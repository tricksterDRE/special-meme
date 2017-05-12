from datetime import datetime
from flask_restful import Resource, reqparse
from meme import db
from meme.models import Task, Report, Photo


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
        parser.add_argument('gps_longitude', type=float, help='longtitude')
        parser.add_argument('gps_latitude', type=float, help='latitude')
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

        return {''}, 200