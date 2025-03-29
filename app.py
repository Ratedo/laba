from flask import Flask, jsonify, request, Response
import json
from collections import OrderedDict
import os

app = Flask(__name__)

def make_contact():
    return OrderedDict([
        ("id", 0),
        ("username", ""),
        ("given_name", ""),
        ("family_name", ""),
        ("full_name", ""),
        ("phone", None),
        ("email", None),
        ("birthdate", "")
    ])

def make_group():
    return OrderedDict([
        ("id", 0),
        ("title", ""),
        ("description", ""),
        ("contacts", [])
    ])

def ordered_json_response(data, status=200):
    return Response(
        json.dumps(data, indent=2),
        status = status,
        mimetype = 'application/json'
    )

# Контакты
@app.route('/api/v1/contact', methods=['GET'])
def get_contacts():
    return ordered_json_response(make_contact())

@app.route('/api/v1/contact', methods=['POST'])
def create_contact():
    return ordered_json_response(make_contact()), 201

@app.route('/api/v1/contact/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    return ordered_json_response(make_contact())

@app.route('/api/v1/contact/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    return ordered_json_response(make_contact())

@app.route('/api/v1/contact/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    return ordered_json_response({}), 204

# Группы
@app.route('/api/v1/group', methods=['GET'])
def get_groups():
    return ordered_json_response(make_group())

@app.route('/api/v1/group', methods=['POST'])
def create_group():
    return ordered_json_response(make_group()), 201

@app.route('/api/v1/group/<int:group_id>', methods=['GET'])
def get_group(group_id):
    return ordered_json_response(make_group())

@app.route('/api/v1/group/<int:group_id>', methods=['PUT'])
def update_group(group_id):
    return ordered_json_response(make_group())

@app.route('/api/v1/group/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    return ordered_json_response({}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6090, debug=True)