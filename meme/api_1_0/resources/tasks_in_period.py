from flask_restful import Resource, reqparse
from flask import jsonify
from datetime import datetime
from meme.models import Task
from meme import ma


class TasksInPeriodSchema(ma.ModelSchema):
    class Meta:
        model = Task
        exclude = ['report']


class TasksInPeriod(Resource):
    """REST API resource for getting list of all tasks created in time period"""

    def __init__(self):
        self.task_schema = TasksInPeriodSchema()

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('period_start', type=str, location='args', help='start time')
        parser.add_argument('period_end', type=str, location='args', help='end time')
        args = parser.parse_args()

        if args['period_start'] is None or args['period_end'] is None:
            return {'error': 'missing required parameter'}, 400

        try:
            period_start = datetime.strptime(args['period_start'], '%Y-%m-%dT%H:%M:%S')
            period_end = datetime.strptime(args['period_end'], '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            return {'error': 'inv'}, 400

        tasks_by_period = Task.query.filter(Task.start_time >= period_start).filter(Task.start_time <= period_end).all()
        data, errors = self.task_schema.dump(tasks_by_period, many=True)

        return jsonify(data)
