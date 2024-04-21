from marshmallow import Schema, fields

class SportmenDeserializeSchema(Schema):
    service = fields.UUID()
    amount = fields.Integer()

class SportmenSerializeSchema(Schema):
    id = fields.UUID()
    service = fields.UUID()
    amount = fields.Integer()