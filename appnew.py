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
    return "Welcome to the Flask API! Use /data to POST, GET, PUT or DELETE data."


@app.route('/data', methods=['POST'])
def add_data():
    # Get the JSON data from the request
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Generate a new ID
    new_id = len(data_storage) + 1
    data['id'] = new_id  # Add an ID field to the data

    # Add the data to the storage
    data_storage.append(data)

    # Write the updated data to the JSON file
    with open(DATA_FILE, 'w') as file:
        json.dump(data_storage, file, indent=4)

    return jsonify({"message": "Data added successfully", "data": data}), 201


@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_storage), 200


@app.route('/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    # Find the data by ID
    data = next((item for item in data_storage if item["id"] == data_id), None)
    if not data:
        return jsonify({"error": "Data not found"}), 404
    return jsonify(data), 200


# Route to get data by specific key-value pair
@app.route('/data/search', methods=['GET'])
def search_data():
    # Get the query parameters
    query_params = request.args

    # Check if no query parameters are provided
    if not query_params:
        return jsonify({"error": "Query parameters are required"}), 400

    # Search for data entries that match the query parameters
    matching_data = [
        item for item in data_storage
        if all(str(item.get(key)) == value for key, value in query_params.items())
    ]

    if not matching_data:
        return jsonify({"error": "No matching data found"}), 404

    return jsonify(matching_data), 200


# Route to update existing data by ID
@app.route('/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    # Get the JSON data from the request
    updated_data = request.get_json()
    if not updated_data:
        return jsonify({"error": "No data provided"}), 400

    # Find the index of the data with the given ID
    data_index = next((index for index, item in enumerate(data_storage) if item["id"] == data_id), None)

    if data_index is None:
        return jsonify({"error": "Data not found"}), 404

    # Update the data
    data_storage[data_index].update(updated_data)

    # Write the updated data to the JSON file
    with open(DATA_FILE, 'w') as file:
        json.dump(data_storage, file, indent=4)

    return jsonify({"message": "Data updated successfully", "data": data_storage[data_index]}), 200


# Route to delete existing data by ID
@app.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    # Find the index of the data with the given ID
    data_index = next((index for index, item in enumerate(data_storage) if item["id"] == data_id), None)

    if data_index is None:
        return jsonify({"error": "Data not found"}), 404

    # Remove the data
    removed_data = data_storage.pop(data_index)

    # Write the updated data to the JSON file
    with open(DATA_FILE, 'w') as file:
        json.dump(data_storage, file, indent=4)

    return jsonify({"message": "Data deleted successfully", "data": removed_data}), 200


if __name__ == '__main__':
    app.run(debug=True)
