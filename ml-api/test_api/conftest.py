import pytest
import json

from api.app import create_app
from api.config import TestingConfig
from ows_language_model.config import config

@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)

    with app.app_context():
        yield app

@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client

@pytest.fixture
def text_input_data():
    return None