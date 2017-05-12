from meme import ma
from meme.models import Engineer, Task


class EngineerSchema(ma.ModelSchema):
    class Meta:
        model = Engineer


class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
