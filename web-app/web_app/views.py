import json
import time

import requests
from flask import Flask, jsonify, render_template, request, url_for, redirect, Blueprint
from flask_cors import CORS, cross_origin

# code template for generating sections of the app

ui_app = Blueprint('frontend', __name__)

#from app import app
CORS(ui_app, support_credentials=True)


@ui_app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def index():
    errors = []
    if request.method == 'POST':
        req = request.form
        #errors.append("The prediction server crashed. Please try again, or upload a smaller JSON file.")
    return render_template("index.html", errors=errors)

