import os

from flask import Flask
from web_app.config import Config, get_logger

_logger = get_logger(logger_name=__name__)

def create_app(*, config_object) -> Flask:
    """ create a flask app instance"""
    flask_app = Flask('web_app')
    flask_app.config.from_object(config_object)
    flask_app.config['CORS_HEADERS'] = 'Content-Type'
    from .views import ui_app
    flask_app.register_blueprint(ui_app)
    
    _logger.debug('Application instance created')
    return flask_app