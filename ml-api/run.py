import os

from api.app import create_app
from api.config import DevelopmentConfig, ProductionConfig


config_object = eval(os.environ['APP_SETTINGS'].split('.')[1])

application = create_app(
    config_object=config_object)

if __name__ == '__main__':
    application.run()