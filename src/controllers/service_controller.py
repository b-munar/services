from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.service_model import ServiceModel
from src.schemas.service_schema import ServiceDeserializeSchema, ServiceSerializeSchema
from src.utils.authorization import authorization

class ServiceController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        service_create_schema = ServiceDeserializeSchema()
        
        errors = service_create_schema.validate(request_json)
        if errors:
            print(errors)
            return "", 400
        
        service_create_dump = service_create_schema.dump(request_json)
        service_create_dump["user"] = kwargs["user"]["id"]
        
        # token = kwargs["token"]
        # If you need to use another microservice,
        # use this token with the request library,
        # remember to paste the Bearer before the token
        
        session = Session()
        new_service = ServiceModel(**service_create_dump)
        session.add(new_service)
        session.commit()

        service_created_schema = ServiceSerializeSchema()
        service_created_dump = service_created_schema.dump(new_service)
        return service_created_dump, 201
    
    def get(self, **kwargs):
        service_schema = ServiceSerializeSchema()

        session = Session()
        query = session.query(ServiceModel).filter(ServiceModel.user==kwargs["user"]["id"])
        session.close()
        
        services = [service_schema.dump(service) for service in query]
        return services, 200

