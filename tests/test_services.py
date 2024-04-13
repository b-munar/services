import pytest
import json
from unittest.mock import patch
from functools import wraps

def mock_authorization(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            kwargs["user"] = {"id" : "9027aff6-545e-4a1c-bbf7-9c09f6ae595c"}
            return func(*args, **kwargs)
    return decorated

patch('src.utils.authorization.authorization', mock_authorization).start()

from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_request_ping(client):
    response = client.get("/services/ping")
    assert response.status_code == 200
    assert b"pong" in response.data
    
def test_request_post(client):
     url = "/services"
     headers = {
        "Content-Type": "application/json"
    }
     data = {
        "name": "service 1",
        "description": "description 1",
        "cost": 20.0,
        "taxes": 5.0,
        "address": "direction",
        "details": "details"
        }
     response = client.post(url, data=json.dumps(data), headers=headers)
     assert response.status_code == 201
     assert b"name" in response.data

def test_request_get(client):
     url = "/services"
     headers = {
        "Content-Type": "application/json"
    }
     data = {
        "name": "service 1",
        "description": "description 1",
        "cost": 20.0,
        "taxes": 5.0,
        "address": "direction",
        "details": "details"
        }
     client.post(url, data=json.dumps(data), headers=headers)
     response = client.get(url)
     assert response.status_code == 200
     assert b"services" in response.data

