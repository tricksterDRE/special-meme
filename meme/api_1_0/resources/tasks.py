from datetime import datetime
from flask_restful import Resource, reqparse
from flask import jsonify
from meme import db
from meme.models import Task, Engineer, Photo, Report
from meme.schemas import task_schema


class TaskById(Resource):
    """REST API resource for getting and updating task by id """

    def get(self, task_id):
        task = Task.query.get(task_id)

        if not task:
            return {'error': 'task not found'}, 404

        return task_schema.jsonify(task)

    def post(self, task_id):
        task = Task.query.get(task_id)

        if not task:
            return {'error': 'task not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('task_name', type=str, help='task description')
        parser.add_argument('task_description', type=str, help='task full description')
        parser.add_argument('start_time', type=str, help='task start time')
        parser.add_argument('photo_required', type=bool, help='are photo required')
        post_args = parser.parse_args()

        task, errors = task_schema.load(jsonify(post_args), instance=task)

        if errors:
            return jsonify(errors), 400

        db.session.add(task)
        db.session.commit()

        return {'status': 'updated', "id": task.id_task}


class Tasks(Resource):
    """REST API resource for getting list of all tasks and creating task for specified engineer"""

    def get(self):
        tasks = Task.query.all()
        data, errors = task_schema.dump(tasks, many=True)
        return jsonify(data)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_engineer', type=int, help='id of the assignee engineer')
        parser.add_argument('task_name', type=str, help='task description')
        parser.add_argument('task_description', type=str, help='task full description')
        parser.add_argument('start_time', type=str, help='task start time')
        parser.add_argument('photo_required', type=bool, help='are photo required')
        post_args = parser.parse_args()

        try:
            assignee_engineer = Engineer.query.get(post_args['id_engineer'])

            if not assignee_engineer:
                return {'error': 'engineer not found'}, 404

            try:
                start_time = datetime.strptime(post_args['start_time'], '%d.%m.%Y %H:%M:%S')
            except ValueError:
                return {'error': 'incorrect date format'}, 400

            task = Task(task_name=post_args['task_name'], task_description=post_args['task_description'],
                        start_time=start_time, photo_required=post_args['photo_required'], engineer=assignee_engineer)

            db.session.add(task)
            db.session.commit()

            return {'status': 'created', 'id': task.id_task}
        except KeyError:
            return {'error': 'missing required parameter'}, 400


class TasksFinalizer(Resource):
    """REST API resource for finishing task with report"""
    def post(self, task_id):
        task = Task.query.get(task_id)

        if not task:
            return {'error': 'task not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('comment', type=str, help='finish comment')
        parser.add_argument('end_time', type=str, help='finish time')
        parser.add_argument('gps_longitude', type=str, help='longtitude')
        parser.add_argument('gps_latitude', type=str, help='latitude')
        parser.add_argument('link', type=str, help='photo link')
        post_args = parser.parse_args()

        post_args.setdefault('link', '')

        try:
            report_args = {
                'comment': post_args['comment'],
                'end_time': post_args['end_time'],
                'gps_longitude': post_args['gps_longitude'],
                'gps_latitude': post_args['gps_latitude'],
                'link': post_args['link']
            }
        except KeyError:
            return {'error': 'missing required parameter'}, 400

        if task.photo_required and report_args['link'] == '':
            return {'error': 'photo link required to finish task'}, 400

        try:
            end_time = datetime.strptime(report_args['end_time'], '%d.%m.%Y %H:%M:%S')
        except ValueError:
            return {'error': 'incorrect date format'}, 400

        report = Report(comment=report_args['comment'], gps_longitude=report_args['gps_longitude'],
                        gps_latitude=report_args['gps_latitude'] ,end_time=end_time, task=task)

        db.session.add(report)

        if task.photo_required:
            photo = Photo(report=report, link=post_args['link'])
            db.session.add(photo)

        db.session.commit()

        return {'status': 'finished', 'id': task.id_task}, 200


class TasksInPeriod(Resource):
    """REST API resource for getting list of all tasks created in time period"""
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('period_start', type=str, help='start time')
        parser.add_argument('period_end', type=str, help='end time')
        post_args = parser.parse_args()

        try:
            period_start = post_args['period_start']
            period_end = post_args['period_end']
        except KeyError:
            return {'error': 'missing required parameter'}, 400

        try:
            period_start = datetime.strptime(period_start, '%d.%m.%Y %H:%M:%S')
            period_end = datetime.strptime(period_end, '%d.%m.%Y %H:%M:%S')
        except ValueError:
            return {'error': 'incorrect date format'}, 400

        tasks_by_period = Task.query.filter(Task.start_time >= period_start).filter(Task.start_time <= period_end).all()
        data, errors = task_schema.dump(tasks_by_period, many=True)

        return jsonify(data)



