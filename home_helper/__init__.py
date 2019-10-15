from flask import Flask
from home_helper.config import ProductionConfig, DevelopmentConfig

# TODO: add tests and testing configuration


def create_app(settings='production'):
    app = Flask(__name__)
    if settings == 'development':
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)
    from home_helper.routes import home_helper
    app.register_blueprint(home_helper)
    return app
