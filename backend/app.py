'''
Date: 2022-03-26 16:39:12
LastEditors: Azus
LastEditTime: 2022-03-28 22:49:03
FilePath: /RF_Template/backend/app.py
'''

import os
from flask import Flask, render_template
from . import reverseProxy as rP

MODE = os.getenv('FLASK_ENV')
DEV_SERVER_URL = 'http://localhost:3000/'

app = Flask(__name__)

# Ignore static folder in development mode.
if MODE == "development":
    app = Flask(__name__, static_folder=None)

@app.route('/')
@app.route('/<path:path>')
def index(path=''):
    if MODE == 'development':
        return rP.proxyRequest(DEV_SERVER_URL, path)
    else:
        return render_template("index.html")    