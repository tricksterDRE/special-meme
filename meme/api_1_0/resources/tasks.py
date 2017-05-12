from datetime import datetime
from flask_restful import Resource, reqparse
from meme import db
from meme.models import Task, Engineer
from meme.schemas import TaskSchema


class TaskResource(Resource):
    """REST API resource for /tasks/<id> """

    def __init__(self):
        self.schema = TaskSchema()

    def get(self, task_id):
        """GET /api/v1/tasks/<id> - returns task data by id"""
        task = Task.query.get(task_id)
        return self.schema.jsonify(task)

    def put(self, task_id):
        """PUT /api/v1/tasks/<id> - updates task data by id"""
        pass


class TasksListResource(Resource):
    """REST API FOR /tasks endpoint"""

    def __init__(self):
        self.schema = TaskSchema()
        pass

    def get(self):
        """GET /api/v1/tasks - return all tasks data"""
        tasks = Task.query.all()
        return self.schema.jsonify(tasks, many=True)

    def post(self):
        """POST /api/v1/tasks - creates task with specified description 
                for specified engineer
        """
        parser = reqparse.RequestParser()
        parser.add_argument('engineer_id', type=int, help='id of the assignee engineer')
        parser.add_argument('description', type=str, help='task description')
        parser.add_argument('full_description', type=str, help='task full description')
        parser.add_argument('start_time', type=str, help='task start time')

        args = parser.parse_args()

        engineer_id = args['engineer_id']
        description = args['description']
        full_description = args['full_description']
        start_time_str = args['start_time']

        if engineer_id is None or description is None or start_time_str is None:
            return {'error': 'missing required parameters'}, 400

        try:
            start_time = datetime.strptime(start_time_str, '%d.%m.%Y %H:%M:%S')
        except ValueError:
            return {'error': 'incorrect start date format {}'.format(start_time_str)}, 400

        assignee_engineer = Engineer.query.get(engineer_id)

        if assignee_engineer is None:
            return {'error': 'incorrect engineer_id'}, 400

        task = Task(description=description, full_description=full_description, start_time=start_time,
                    engineer=assignee_engineer)

        db.session.add(task)
        db.session.commit()

        return self.schema.jsonify(task)




