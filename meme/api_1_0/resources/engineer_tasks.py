from flask_restful import Resource
from flask import jsonify
from meme.models import Engineer, Task
from meme import ma


class EngineerTasksSchema(ma.ModelSchema):
    """Marshmallow "serialization schema for Task db Table"""
    class Meta:
        model = Task
        exclude = ['report']


class EngineerTasks(Resource):
    """REST API resource for getting list of engineers tasks"""

    def __init__(self):
        self.schema = EngineerTasksSchema()

    def get(self, engineer_id):
        engineer = Engineer.query.get(engineer_id)

        if not engineer:
            return {'error': 'engineer not found'}, 404

        all_tasks = Task.query.filter_by(engineer=engineer, report=None)

        data, errors = self.schema.dump(all_tasks, many=True)

        return jsonify(data)
