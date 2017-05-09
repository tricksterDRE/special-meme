from meme import ma
from meme.models import Engineer


class EngineerSchema(ma.ModelSchema):
    class Meta:
        model = Engineer
