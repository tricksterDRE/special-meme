from flask_restful import Resource
from meme.models import Task, Engineer
from meme.schemas import TaskSchema


class EngineersTasksResource(Resource):
    """REST API resource for /engineers/<int:engineer_id>/tasks"""
    def __init__(self):
        self.schema = TaskSchema()

    def get(self, engineer_id):
        engineer = Engineer.query.get(engineer_id)
        tasks = Task.query.filter_by(engineer=engineer)

        return self.schema.jsonify(tasks, many=True)
