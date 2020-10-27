
from ows_language_model import __version__ as _version
from api import __version__ as api_version

import json
import pathlib
# import math

from api import __version__ as api_version


THIS_DIR = pathlib.Path().resolve()

def test_health_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/health')

    # Then
    assert response.status_code ==200

def test_prediction_endpoint_returns_prediction(flask_test_client, text_input_data):
    # Given
    # Load the test data from the copies filed IE package

    #_X, _y = load_dataset(filename=)
    
    # When
    response = flask_test_client.post('/v1/predict/language_model',
                                      json=text_input_data)

    # Then
    assert response.status_code ==200
    response_json = json.loads(response.data)
    predictions = response_json['predictions']
    response_version = response_json['version']
    assert predictions

def test_version_endpoint_returns_versions(flask_test_client):
    # Given
    model_version = _version

    # When
    response = flask_test_client.get('/version')

    # Then
    response_json = json.loads(response.data)
    assert response.status_code == 200
    assert response_json.get('model_version') == _version
    assert response_json.get('api_version') == api_version