from flask import Blueprint, request, jsonify
import json 
from flask_cors import CORS, cross_origin

from ows_language_model.predict import make_single_prediction
from ows_language_model import __version__ as _version
from . import __version__ as api_version
from .config import get_logger

_logger = get_logger(logger_name=__name__)

# code template for generating sections of the app
prediction_app = Blueprint('prediction_app', __name__)


cors = CORS(prediction_app, 
                resources={r"/v1/predict/language_model": 
                            {"origins": "http://localhost:5000"}})




@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info("health status OK")
        return 'ok'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        resp = jsonify({'model_version': _version,
                        'api_version': api_version})
        return resp


@prediction_app.route('/v1/predict/language_model', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def predict():
    if request.method == 'POST':
        json_data = request.get_data()
        if type(json_data) != dict:
            json_data = json.loads(json_data)

        _logger.info(f'Inputs: {json_data}')
        count = int(json_data['count'])
        if count>0:
            sentence = " ".join([json_data['context'], json_data['textInput']])
        else:
            sentence = json_data['textInput']
            
        result = make_single_prediction(input_text=sentence)
        
        _logger.info(f'Outputs: {result}')

        predictions = result.get('predictions')
        version = result.get('version')
        resp = jsonify({'predictions': predictions,
                        'version': version,
                        'count' : count+1})

        return resp

