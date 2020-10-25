import time

import requests
from flask import Flask, jsonify, render_template, request, url_for, redirect
from flask_cors import CORS, cross_origin

import json
import time

from app import app
CORS(app, support_credentials=True)


@app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def index():
    errors = []
    if request.method == 'POST':
        req = request.form
        #errors.append("The prediction server crashed. Please try again, or upload a smaller JSON file.")
    return render_template("index.html", errors=errors)

