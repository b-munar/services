from marshmallow import Schema, fields

class ServiceDeserializeSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=True)
    cost = fields.Float(required=True)
    taxes = fields.Float(required=True)
    address = fields.String(required=True)
    details = fields.String(required=True)

class ServiceSerializeSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    description = fields.String()
    cost = fields.Float()
    taxes = fields.Float()
    address = fields.String()
    details = fields.String()
    updateAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')
    createdAt = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z')
