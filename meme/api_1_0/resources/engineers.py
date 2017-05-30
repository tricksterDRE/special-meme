from flask_restful import Resource, reqparse
from meme import db, ma
from meme.models import Engineer


class EngineerSchema(ma.ModelSchema):
    """Marshmallow "serialization schema for Engineer db Table"""
    class Meta:
        model = Engineer
        exclude = ["tasks"]


class Engineers(Resource):
    """REST API resource for getting list of all engineers and creating engineer"""

    def __init__(self):
        self.engineer_schema = EngineerSchema()

    def get(self):
        all_engineers = Engineer.query.all()
        data, errors = self.engineer_schema.dump(all_engineers, many=True)

        return data

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('full_name', type=str, help='name of the engineer')
        post_args = parser.parse_args()

        engineer, errors = self.engineer_schema.load(post_args)

        if errors:
            return {'status': 'error', 'error': 'missing required parameter'}, 400

        db.session.add(engineer)
        db.session.commit()

        return {'status': 'created', 'id': engineer.id_engineer}, 200
