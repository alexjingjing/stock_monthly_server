# -*- encoding: utf-8 -*-
"""
stock server powered by flask in Python 3.6+

__author__ = 'liusiming'
__date__ = '2018-02-11'
"""
import json
import os

from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore, utils

from app.controller.stock import stock
from app.exception.invalidusage import InvalidUsage
from app.models.database import session, init_db
from app.models.role import Role
from app.models.user import User

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(stock)
# Set config values for Flask-Security.
# We're using PBKDF2 with salt.
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
# Replace this with your own salt.
app.config['SECURITY_PASSWORD_SALT'] = 'o!iB%uW12'

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(session,
                                                User, Role)
security = Security(app, user_datastore)


# Create a user to test with
@app.before_first_request
def create_user():
    init_db()
    # Create the Roles "admin" and "end-user" -- unless they already exist
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='end-user', description='End user')
    session.commit()

    encrypted_pass = utils.hash_password('password')
    if not User.query.first():
        user_datastore.create_user(email='guan2359@gmail.com', password=encrypted_pass)
        session.commit()

    user_datastore.add_role_to_user('guan2359@gmail.com', 'end-user')
    session.commit()


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def func_task():
    """
    CRUD
    """
    # GET 返回 task 列表
    if request.method == 'GET':
        data = [
            'THIS IS GET METHOD'
        ]

    # POST 创建新的任务
    if request.method == 'POST':
        data = [
            'THIS IS POST METHOD'
        ]

    # PUT 更改任务
    if request.method == 'PUT':
        data = [
            'THIS IS PUT METHOD'
        ]

    # DELETE 删除任务
    if request.method == 'DELETE':
        data = [
            'THIS IS DELETE METHOD'
        ]

    resp = make_response(json.dumps({
        'code': 1000,
        'data': data
    }))
    resp.headers['Content-Type'] = 'application/json'
    return resp, 200


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=8888, debug=True)
