from flask_restful import Resource, reqparse
from datetime import datetime
from meme.models import Task, Report, Photo
from meme import db, ma


class TasksFinalizer(Resource):
    """REST API resource for finishing task with report"""
    def post(self, task_id):
        task = Task.query.get(task_id)

        if not task:
            return {'status': 'error', 'error': 'task not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('comment', type=str, help='finish comment')
        parser.add_argument('end_time', type=str, help='finish time')
        parser.add_argument('gps_longitude', type=str, help='longtitude')
        parser.add_argument('gps_latitude', type=str, help='latitude')
        parser.add_argument('link', type=str, help='photo link')
        post_args = parser.parse_args()

        if post_args['comment'] is None or post_args['end_time'] is None or post_args['gps_longitude'] is None or post_args['gps_latitude'] is None:
            return {'status': 'error', 'error': 'missing required parameter'}, 400

        if task.photo_required and (post_args['link'] is None or post_args['link'] == ''):
            return {'status': 'error', 'error': 'missing required parameter'}, 400

        try:
            end_time = datetime.strptime(post_args['end_time'], '%Y-%m-%dT%H:%M:%S+00:00')
        except ValueError:
            return {'status': 'error', 'error': 'missing required parameter'}, 400

        if Report.query.filter_by(id_task=task_id).first() is not None:
            return {'status': 'error', 'error': 'task already closed'}, 400

        report = Report(comment=post_args['comment'], gps_longitude=post_args['gps_longitude'],
                    gps_latitude=post_args['gps_latitude'] ,end_time=end_time, task=task)

        db.session.add(report)

        if task.photo_required:
            photo = Photo(report=report, link=post_args['link'])
            db.session.add(photo)

        db.session.commit()

        return {'status': 'finished', 'id': task.id_task}, 200