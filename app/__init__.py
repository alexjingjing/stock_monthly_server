# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient

client = MongoClient('123.207.58.71', 27017)
stock = client.stock
stockItem = stock.stockItem
