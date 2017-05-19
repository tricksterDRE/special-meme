from datetime import datetime
from flask_restful import Resource, reqparse
from meme import db
from meme.models import Task, Engineer, Photo, Report
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

        task = Task(task_name=description, task_description=full_description, start_time=start_time,
                    engineer=assignee_engineer)

        db.session.add(task)
        db.session.commit()

        return self.schema.jsonify(task)


class TasksFinishResource(Resource):
    def __init__(self):
        pass

    def post(self, task_id):
        task = Task.query.get(task_id)

        if task is None:
            return {'error': 'incorrect input sequence, use Einstein-Shrodinger quantum sequencer'}, 400

        parser = reqparse.RequestParser()
        parser.add_argument('comment', type=str, help='finish comment')
        parser.add_argument('end_time', type=str, help='finish time')
        parser.add_argument('gps_longitude', type=str, help='longtitude')
        parser.add_argument('gps_latitude', type=str, help='latitude')
        parser.add_argument('photo_link', type=str, help='photo link')

        args = parser.parse_args()

        comment = args['comment']
        end_time_str = args['end_time']
        gps_longitude = args['gps_longitude']
        gps_latitude = args['gps_latitude']
        photo_link = args['photo_link']

        try:
            end_time = datetime.strptime(end_time_str, '%d.%m.%Y %H:%M:%S')
        except ValueError:
            return {'error': 'incorrect start date format {}'.format(end_time_str)}, 400

        finish_report = Report(comment=comment, gps_longitude=gps_longitude, gps_latitude=gps_latitude,
                               end_time=end_time, task=task)

        db.session.add(finish_report)

        if photo_link is not None:
            photo = Photo(report=finish_report, link=photo_link)
            db.session.add(photo)

        db.session.commit()

        return {}, 200


class TasksTimeResource(Resource):
    def __init__(self):
        self.schema = TaskSchema()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('period_start', type=str, help='start time')
        parser.add_argument('period_end', type=str, help='end time')

        args = parser.parse_args()

        period_start = args['period_start']
        period_end = args['period_end']

        try:
            period_start = datetime.strptime(period_start, '%d.%m.%Y %H:%M:%S')
            period_end = datetime.strptime(period_end, '%d.%m.%Y %H:%M:%S')
        except ValueError:
            return {'error': 'incorrect start date format {} {}'.format(period_start, period_end)}, 400

        tasks_by_period = Task.query.filter(Task.start_time >= period_start).filter(Task.start_time <= period_end).all()

        return self.schema.jsonify(tasks_by_period, many=True)



