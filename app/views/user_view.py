# In views/user_view.py
from flask import jsonify, Blueprint, request
from app.models.user_model import register_user, authenticate_user

user_view_api = Blueprint('user_view_api', __name__)

@user_view_api.route('/api/users/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    register_user(username, password)
    return jsonify({'message': 'User registered successfully'}), 201

@user_view_api.route('/api/users/login', methods=['POST','GET'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = authenticate_user(username, password)
    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401