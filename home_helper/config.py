import os

MY_SECRET_KEY = os.environ.get('SECRET_KEY')

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = MY_SECRET_KEY if MY_SECRET_KEY else 'YOU/SHOULD/SET/A/SECRET/ENVVARIABLE'


class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    FLASK_ENV = 'development'
