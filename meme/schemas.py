from meme import ma
from meme.models import Engineer, Task, Report, Photo


class PhotoSchema(ma.ModelSchema):
    """Marshmallow serialization schema for Photo db table"""
    class Meta:
        model = Photo
        exclude = ["id_photo", "id_report"]


class ReportSchema(ma.ModelSchema):
    """Marshmallow "serialization schema for Report db Table"""
    photo = ma.Nested(PhotoSchema, many=True)

    class Meta:
        model = Report
        exclude = ["id_report", "id_task"]


class TaskSchema(ma.ModelSchema):
    """Marshmallow "serialization schema for Task db Table"""
    report = ma.Nested(ReportSchema, many=True)

    class Meta:
        model = Task
        exclude = ["id_engineer"]


class EngineerSchema(ma.ModelSchema):
    """Marshmallow "serialization schema for Engineer db Table"""
    class Meta:
        model = Engineer
        exclude = ["tasks"]

photo_schema = PhotoSchema()
report_schema = ReportSchema()
task_schema = TaskSchema()
engineer_schema = EngineerSchema()
