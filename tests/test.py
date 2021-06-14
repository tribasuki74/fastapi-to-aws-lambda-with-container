from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_01_main():

    response = client.get("/")
    
    assert str == type(response.json())
    assert response.json() == "Welcome to Test Lambda Function with Docker Container"
    assert response.status_code == 200

def test_02_hello():

    response = client.get("/hello")

    assert str == type(response.json())
    assert response.json() == "Hello Test Lambda Function with Docker Container"
    assert response.status_code == 200