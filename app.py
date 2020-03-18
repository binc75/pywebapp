#!/usr/bin/env python3

#
# Flask REST API for testing purpose
#
#

# RUN:
#  export FLASK_APP=app.py
#  flask run

import datetime
import json
import os
from flask import Flask,jsonify

# Init app
app = Flask(__name__)

# Vars
appVersion = os.environ.get("VERSION")
author = "bianchi.nicola@gmail.com"



# http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    '''Return basic informations'''
    #myHostName = os.uname()[1]
    myHostName = os.uname()
    return jsonify({'message': 'Hello World',
                    'sysinfo': myHostName,
                    'version': appVersion,
                    'route': ['/version', '/date', '/user'],
                    'author': author,
                    }), 200


# http://127.0.0.1:5000/version
@app.route('/version')
def version():
    '''Return version from os environment variable "VERSION"'''
    return jsonify({'version': appVersion}), 200


# http://127.0.0.1:5000/date
@app.route('/date')
def return_date():
    '''Return current date'''
    return jsonify({'date': str(datetime.date.today())}), 200


# http://127.0.0.1:5000/user/nbianchi1
@app.route('/user/<username>')
def get_user(username):
    '''Return username passed as url'''
    return jsonify({'username': str(username)}), 200



# App parameters
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
