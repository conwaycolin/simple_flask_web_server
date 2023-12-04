import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client    

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Bethlehem, PA</h1>" in response.data

def test_get_temperature_route(client):
    response = client.get("/get_temperature")
    assert response.status_code == 200

def test_get_conditions_route(client):
    response = client.get("/get_conditions")
    assert response.status_code == 200

