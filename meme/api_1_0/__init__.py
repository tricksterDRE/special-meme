from flask import Blueprint
import flask_restful

API_VERSION_V1 = 1

api_bp = Blueprint('api', __name__)
api_v1 = flask_restful.Api(api_bp)
