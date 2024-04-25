from marshmallow import Schema, fields
from schemas.service_schema import ServiceDeserializeSchema

class SportmenDeserializeSchema(Schema):
    service_id = fields.UUID(required=True)
    amount = fields.Integer(required=True)
    date = fields.String(required=True)

class SportmenSerializeSchema(Schema):
    id = fields.UUID()
    service_id = fields.UUID()
    amount = fields.Integer()
    date = fields.String()
    service = fields.Nested(ServiceDeserializeSchema)
    # service = fields.Dict()