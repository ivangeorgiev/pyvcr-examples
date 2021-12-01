import marshmallow
from marshmallow import fields
from . import model

class PersonSchema(marshmallow.Schema):
    name = fields.String()
    height = fields.Integer(allow_none=True)
    mass = fields.Float(allow_none=True)
    hair_color = fields.String()
    skin_color = fields.String()
    eye_color = fields.String()
    birth_year = fields.String()
    gender = fields.String()

    class Meta:
        # See https://marshmallow.readthedocs.io/en/stable/quickstart.html#handling-unknown-fields
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def to_object(self, data, **kwargs):
        return model.Person(**data)

    def load(self, data, *args, **kwargs):
        if data['height'] == 'unknown':
            data['height'] = None
        if data['mass'] == 'unknown':
            data['mass'] = None
        else:
            data['mass'] = data['mass'].replace(',', '')
        return super().load(data, *args, **kwargs)