#!flask/bin/python

from migrate.versioning import api
from config import config

api.upgrade(config['default'].SQLALCHEMY_DATABASE_URI, config['default'].SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(config['default'].SQLALCHEMY_DATABASE_URI, config['default'].SQLALCHEMY_MIGRATE_REPO)

print('Current database version: ' + str(v))