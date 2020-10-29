#!/usr/bin/env python3

#
# Flask REST API for testing purpose
#
#

# RUN:
#  export FLASK_APP=app.py
#  flask run

import datetime
import os
from flask import Flask, jsonify, request, make_response

# Init app
app = Flask(__name__)

# Vars
appVersion = os.environ.get("VERSION")
author = "bianchi.nicola@gmail.com"


# http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    '''Return basic informations'''
    myHostName = os.uname()
    return jsonify({'message': 'Hello World',
                    'sysinfo': myHostName,
                    'version': appVersion,
                    'routes': ['/version', '/headers', '/date', '/user/<string>', '/cookie'],
                    'author': author,
                    }), 200


# http://127.0.0.1:5000/version
@app.route('/version')
def version():
    '''Return version from os environment variable "VERSION"'''
    return jsonify({'version': appVersion}), 200


# http://127.0.0.1:5000/headers
@app.route('/headers')
def headers():
    '''Return request HTTP headers'''
    headersDict = dict(request.headers)
    return jsonify(headersDict), 200


# http://127.0.0.1:5000/date
@app.route('/date')
def return_date():
    '''Return current date'''
    return jsonify({'date': str(datetime.date.today()),
                    'time': str(datetime.datetime.now()).split(' ')[1]}), 200


# http://127.0.0.1:5000/user/nbianchi1
@app.route('/user/<username>')
def get_user(username):
    '''Return username passed as url'''
    return jsonify({'username': str(username)}), 200


# http://127.0.0.1:5000/cookie
# Give you back a cookie
@app.route('/cookie')
def cookie():
    if not request.cookies.get('canary'):
        res = make_response("Setting a cookie")
        res.set_cookie('canary', 'betatester', max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response("Value of cookie canary is: {}".format(request.cookies.get('canary')))
    return res


# App parameters
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
