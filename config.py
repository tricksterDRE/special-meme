import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP_DIR = os.path.abspath(os.path.realpath(__file__))
    SECRET_KEY = 'special_memes_supreme'

    SQLALCHEMY_DATABASE_URI = "postgresql://andrey:1234567890@78.155.217.63:5432/bluntman"
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG_TOOLBAR_ENABLED = True
    REST_URL_PREFIX = '/api'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}