#!/usr/bin/python

from migrate.versioning import api
from config import config
from meme import db
import os.path

db.create_all()

if not os.path.exists(config['default'].SQLALCHEMY_MIGRATE_REPO):
    api.create(config['default'].SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(config['default'].SQLALCHEMY_DATABASE_URI, config['default'].SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(config['default'].SQLALCHEMY_DATABASE_URI, config['default'].SQLALCHEMY_MIGRATE_REPO,
                        api.version(config['default'].SQLALCHEMY_MIGRATE_REPO))
