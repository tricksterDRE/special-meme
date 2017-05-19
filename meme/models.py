from meme import db


class Engineer(db.Model):
    """Database model for engineers."""

    __tablename__ = 'Engineers'

    id_engineer = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String())
    tasks = db.relationship('Task', backref='engineer', lazy='dynamic')

    def __init__(self, full_name):
        self.full_name = full_name

    def __repr__(self):
        return '<id {}'.format(self.id_engineer)


class Task(db.Model):
    """Database model for engineer's tasks."""

    __tablename__ = 'Tasks'

    id_task = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_engineer = db.Column(db.Integer, db.ForeignKey('Engineers.id_engineer'))

    task_name = db.Column(db.String())
    task_description = db.Column(db.String())
    start_time = db.Column(db.DateTime)

    report = db.relationship('Report', backref='task', lazy='dynamic')

    def __init__(self, task_name, task_description, start_time, engineer):
        self.task_name = task_name
        self.task_description = task_description
        self.start_time = start_time
        self.engineer = engineer

    def __repr__(self):
        return '<id {}'.format(self.id_task)


class Report(db.Model):
    """Database model for task's finishing reports"""

    __tablename__ = 'Reports'

    id_report = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_task = db.Column(db.Integer, db.ForeignKey('Tasks.id_task'))

    comment = db.Column(db.String())
    end_time = db.Column(db.DateTime)
    gps_longitude = db.Column(db.Float)
    gps_latitude = db.Column(db.Float)

    photo = db.relationship('Photo', backref='report', lazy='dynamic')

    def __init_(self, comment, end_time, gps_longitude, gps_latitude, task):
        self.comment = comment
        self.end_time = end_time
        self.gps_latitude = gps_latitude
        self.gps_longitude = gps_longitude
        self.task = task

    def __repr__(self):
        return '<id {}'.format(self.id_report)


class Photo(db.Model):
    """Database model for photo (image) attached to report"""

    __tablename__ = 'Photos'

    id_photo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_report = db.Column(db.Integer, db.ForeignKey('Reports.id_report'))

    link = db.Column(db.String())

    def __init__(self, report, link):
        self.report = report
        self.link = link

    def __repr__(self):
        return '<id {}'.format(self.id_photo)
