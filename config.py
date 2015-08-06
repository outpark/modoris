# -*- coding: utf-8 -*-
import os

MONGO_URL = 'mongodb://localhost:27017/'

SECRET_KEY = os.urandom(24)
CSRF_ENABLED = True