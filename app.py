from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# In-memory storage for the entered data
data_storage = []

# Path to the JSON file
DATA_FILE = 'data.json'

# Load existing data from the JSON file, if it exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        data_storage = json.load(file)


@app.route('/')
def index():
    return "Welcome to the Flask API! Use /data to POST or GET data."


@app.route('/data', methods=['POST'])
def add_data():
    # Get the JSON data from the request
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Add the data to the storage
    data_storage.append(data)

    # Write the updated data to the JSON file
    with open(DATA_FILE, 'w') as file:
        json.dump(data_storage, file, indent=4)

    return jsonify({"message": "Data added successfully", "data": data}), 201


@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_storage), 200


if __name__ == '__main__':
    app.run(debug=True)
