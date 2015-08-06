# -*- coding: utf-8 -*-


from config import MONGO_URL
from pymongo import MongoClient
import urllib.parse

client = MongoClient(MONGO_URL)
db = client[urllib.parse(MONGO_URL).path[1:]]
collection = db["Index"]

from crawler import crawl_web