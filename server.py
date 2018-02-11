# -*- encoding: utf-8 -*-
"""
stock server powered by flask in Python 3.6+

__author__ = 'liusiming'
__date__ = '2018-02-11'
"""
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from app.controller.stock import stock
import json

from app.exception.invalidusage import InvalidUsage

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(stock)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
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
    app.run(host='0.0.0.0', port=8888, debug=True)
