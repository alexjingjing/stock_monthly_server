# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, redirect
from pymongo import DESCENDING, ASCENDING
from app import stockItem
import re

stock = Blueprint('stock', __name__)


@stock.route('/stocks', methods=['GET'])
def get_stock_list():
    time_str = request.args['time']
    time_re = re.compile('\d{6}' + time_str)
    s_list = []
    for s in stockItem.find({"date": time_re}, {"_id": 0, "createTime": 0})\
            .sort([("createTime", ASCENDING)]):
        s_list.append(s)
    return jsonify({"errorCode": 0, "stockList": s_list})
