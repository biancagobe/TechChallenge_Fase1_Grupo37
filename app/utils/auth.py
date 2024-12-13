from app import app, auth
from flask import Flask, request, jsonify
from flask_httpauth import HTTPTokenAuth
import jwt
import datetime

@auth.verify_token
def verify_token(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return data['user_id']
    except:
        return None

@app.route('/login', methods=['POST'])
def login():
    auth_data = request.get_json()
    if auth_data and auth_data['username'] == 'user' and auth_data['password'] == 'pass':
        token = jwt.encode({
            'user_id': auth_data['username'],
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/protected', methods=['GET'])
@auth.login_required
def protected():
    return jsonify({'message': 'This is a protected route'})
  