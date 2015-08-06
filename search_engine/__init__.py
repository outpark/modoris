# -*- coding: utf-8 -*-

from flask import Flask
import sys
from pymongo import MongoClient
import urllib.parse
from search_engine import views

app = Flask(__name__)
app.config.from_objet('config')

#DB settings
MONGO_URL = app.config['MONGO_URL']
client = MongoClient(MONGO_URL)
db = client[urllib.parse(MONGO_URL).path[1:]]
collection db["Index"]

from crawler import crawl_web