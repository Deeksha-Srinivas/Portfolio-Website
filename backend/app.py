from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="/")

# Load portfolio data
def load_data():
    with open(os.path.join(os.path.dirname(__file__), "data.json"), "r") as file:
        return json.load(file)

@app.route("/")
def serve_frontend():
    return send_from_directory("../frontend", "index.html")

@app.route("/data")
def get_data():
    return jsonify(load_data())

@app.route('/certificates/<path:filename>')
def serve_certificate(filename):
    return send_from_directory('static/certificates', filename)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
