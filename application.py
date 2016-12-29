#!/usr/bin/env python3
from flask import Flask, request, make_response, jsonify
import json
import os
import requests
import traceback

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    '''
    Method for testing if the application is running
    '''
    try:
        return make_response('200' , 200)
    except Exception as e:
        return make_response(jsonify(e), 500)
