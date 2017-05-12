from flask_restful import Resource, reqparse
from meme import db
from meme.models import Engineer, Task
from meme.schemas import EngineerSchema, TaskSchema


class EngineerResource(Resource):
    """REST API resource for /engineers/<id> endpoint"""

    def __init__(self):
        self.schema = EngineerSchema()

    def get(self, engineer_id):
        """GET /api/v1/engineers/<id> - returns engineer's data by it's id"""
        engineer = Engineer.query.get(engineer_id)
        return self.schema.jsonify(engineer)


class EngineersListResource(Resource):
    """REST API resource for /engineers endpoint"""

    def __init__(self):
        self.schema = EngineerSchema()

    def get(self):
        """GET /api/v1/engineers - returns list of all engineers"""
        engineers = Engineer.query.all()

        return self.schema.jsonify(engineers, many=True)

    def post(self):
        """POST /api/v1/engineers - creates engineer with specified name"""
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='name of the engineer')
        engineer_name = parser.parse_args()['name']

        if engineer_name is not None:
            engineer = Engineer(name=engineer_name)

            db.session.add(engineer)
            db.session.commit()

            return self.schema.jsonify(engineer)
        else:
            return {}, 400


class EngineersTasksResource(Resource):
    """REST API resource for /engineers/<int:engineer_id>/tasks"""
    def __init__(self):
        self.schema = TaskSchema()

    def get(self, engineer_id):
        engineer = Engineer.query.get(engineer_id)
        tasks = Task.query.filter_by(engineer=engineer)

        return self.schema.jsonify(tasks, many=True)