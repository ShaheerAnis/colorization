from marshmallow import fields, Schema


class ImagesSchema(Schema):
    name = fields.String()
    image_file = fields.Raw(type='file', required=True)
