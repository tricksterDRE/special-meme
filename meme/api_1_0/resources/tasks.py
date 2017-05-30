from datetime import datetime
from flask_restful import Resource, reqparse
from flask import jsonify
from meme import db, ma
from meme.models import Task, Engineer


class TaskSchema(ma.ModelSchema):
    """Marshmallow "serialization schema for Task db Table"""
    class Meta:
        model = Task


class Tasks(Resource):
    """REST API resource for getting list of all tasks and creating task for specified engineer"""

    def __init__(self):
        self.task_schema = TaskSchema()

    def get(self):
        tasks = Task.query.all()
        data, errors = self.task_schema.dump(tasks, many=True)
        return jsonify(data)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_engineer', type=int, help='id of the assignee engineer')
        parser.add_argument('task_name', type=str, help='task description')
        parser.add_argument('task_description', type=str, help='task full description')
        parser.add_argument('start_time', type=str, help='task start time')
        parser.add_argument('photo_required', type=bool, help='are photo required')
        post_args = parser.parse_args()

        if post_args['task_name'] is None or post_args['task_description'] is None or post_args['photo_required'] is None or post_args['id_engineer'] is None:
            return {'status': 'error', 'error': 'missing required parameter'}, 400

        assignee_engineer = Engineer.query.get(post_args['id_engineer'])

        if not assignee_engineer:
            return {'status': 'error', 'error': 'engineer not found'}, 404

        start_time = post_args['start_time']

        if start_time is None:
            start_time = datetime.now(tz=None)
        else:
            start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S+00:00')

        task = Task(task_name=post_args['task_name'], task_description=post_args['task_description'],
                    start_time=start_time, photo_required=post_args['photo_required'], engineer=assignee_engineer)

        db.session.add(task)
        db.session.commit()

        return {'status': 'created', 'id': task.id_task}
