from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config

app = Flask(__name__)
app.config.from_object(config['default'])

try:
    from flask_debugtoolbar import DebugToolbarExtension
    DebugToolbarExtension(app)
except:
    pass

db = SQLAlchemy(app)
ma = Marshmallow(app)

from meme.api_1_0 import api_bp, API_VERSION_V1
app.register_blueprint(api_bp, url_prefix='{prefix}/v{version}'.format(prefix=app.config['REST_URL_PREFIX'],
                                                                       version=API_VERSION_V1))

import meme.api_1_0.routes
