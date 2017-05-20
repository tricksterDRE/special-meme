from flask_restful import Resource, reqparse
from flask import jsonify
from meme import db
from meme.models import Engineer, Task
from meme.schemas import engineer_schema, task_schema


class EngineerById(Resource):
    """REST API resource for getting engineer by id"""

    def get(self, engineer_id):
        engineer = Engineer.query.get(engineer_id)

        if not engineer:
            return {}, 404

        data, errors = engineer_schema.jsonify(engineer)

        if errors:
            return jsonify(errors), 404

        return jsonify(data)


class Engineers(Resource):
    """REST API resource for getting list of all engineers and creating engineer"""

    def get(self):
        all_engineers = Engineer.query.all()
        data, errors = engineer_schema.dump(all_engineers, many=True)

        return data

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('full_name', type=str, help='name of the engineer')
        post_args = parser.parse_args()

        engineer, errors = engineer_schema.load(post_args)

        if errors:
            return jsonify(errors), 400

        db.session.add(engineer)
        db.session.commit()

        return {"id": engineer.id_engineer}


class EngineerTasksList(Resource):
    """REST API resource for getting list of engineers tasks"""

    def get(self, engineer_id):
        engineer = Engineer.query.get(engineer_id)

        if not engineer:
            return {}, 404

        all_tasks = Task.query.filter_by(Task.id_engineer == engineer)
        data, errors = task_schema.dump(all_tasks, many=True)

        return data