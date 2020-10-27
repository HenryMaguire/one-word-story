import os

from web_app.app import create_app
from web_app.config import DevelopmentConfig, ProductionConfig, get_logger


_logger = get_logger(logger_name=__name__)

config_object = eval(os.environ['APP_SETTINGS'].split('.')[1])

application = create_app(config_object=config_object)

if __name__ == '__main__':
    application.run()