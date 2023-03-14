import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg123456"
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'superhero'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"


class ProductionConfig(BaseConfig):
    pass
