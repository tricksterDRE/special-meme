from meme import db


class Engineer(db.Model):
    """Database model for engineers."""

    __tablename__ = 'Engineers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    tasks = db.relationship('Task', backref='engineer', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}'.format(self.id)


class Task(db.Model):
    """Database model for engineer's tasks."""

    __tablename__ = 'Tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    engineer_id = db.Column(db.Integer, db.ForeignKey('Engineers.id'))

    description = db.Column(db.String())
    full_description = db.Column(db.String())
    start_time = db.Column(db.DateTime)

    report = db.relationship('Report', backref='task', lazy='dynamic')

    def __init__(self, description, full_description, start_time, engineer):
        self.description = description
        self.full_description = full_description
        self.start_time = start_time
        self.engineer = engineer

    def __repr__(self):
        return '<id {}'.format(self.id)


class Report(db.Model):
    """Database model for task's finishing reports"""

    __tablename__ = 'Reports'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.Integer, db.ForeignKey('Tasks.id'))

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
        return '<id {}'.format(self.id)


class Photo(db.Model):
    """Database model for photo (image) attached to report"""

    __tablename__ = 'Photos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    report_id = db.Column(db.Integer, db.ForeignKey('Reports.id'))

    link = db.Column(db.String())

    def __init__(self, report, link):
        self.report = report
        self.link = link

    def __repr__(self):
        return '<id {}'.format(self.id)
