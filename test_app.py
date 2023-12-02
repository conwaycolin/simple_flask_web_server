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

def test_get_number(client):
    response = client.get("/get_number")
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert 'number' in data
    assert isinstance(data['number'], int)