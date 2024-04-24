from marshmallow import Schema, fields
from schemas.service_schema import ServiceDeserializeSchema

class SportmenDeserializeSchema(Schema):
    service_id = fields.UUID()
    amount = fields.Integer()

class SportmenSerializeSchema(Schema):
    id = fields.UUID()
    service_id = fields.UUID()
    amount = fields.Integer()
    service = fields.Nested(ServiceDeserializeSchema)
    # service = fields.Dict()