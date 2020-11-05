import os
from fastapi.testclient import TestClient
from main import app

# Init client
client = TestClient(app)


def test_root():
    '''Test / path'''
    response = client.get("/")
    data = response.json()
    assert response.status_code == 200
    assert data['message'] == "Hello World!"


def test_version():
    '''Test version path'''
    os.environ["VERSION"] = "100"
    response = client.get("/version", )
    assert response.status_code == 200
    # assert data['version'] == "100"


def test_payload():
    '''Test payload path'''
    response = client.post("/payload/test", json={
        "name": "xstring",
        "description": "string",
        "price": 0})
    data = response.json()
    assert response.status_code == 200
    assert data['payload']['name'] == "xstring"
