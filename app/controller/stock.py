# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, redirect
from app import stockItem
import re

stock = Blueprint('stock', __name__)


@stock.route('/stocks', methods=['GET'])
def get_stock_list():
    time_str = request.args['time']
    time_re = re.compile('\d{6}' + time_str)
    for s in stockItem.find({"date": time_re}):
        print(s)
    return 'yeah'
