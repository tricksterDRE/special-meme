from meme import ma
from meme.models import Engineer, Task, Report, Photo


class PhotoSchema(ma.ModelSchema):
    class Meta:
        model = Photo


class ReportSchema(ma.ModelSchema):
    photo = ma.Nested(PhotoSchema, many=True)

    class Meta:
        model = Report


class TaskSchema(ma.ModelSchema):
    report = ma.Nested(ReportSchema, many=True)

    class Meta:
        model = Task


class EngineerSchema(ma.ModelSchema):
    tasks = ma.Nested(TaskSchema, many=True)

    class Meta:
        model = Engineer


