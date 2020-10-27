import pytest
import json
from web_app.app import create_app
from web_app.config import TestingConfig

@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)
    with app.app_context():
        yield app

@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client