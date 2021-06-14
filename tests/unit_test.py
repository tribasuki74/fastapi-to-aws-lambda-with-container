from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_01_main():

    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"message":"Welcome to Test Lambda Function with Docker Container"}

def test_02_hello():

    response = client.get("/hello")

    assert response.json() == {"message":"Hello Test Lambda Function with Docker Container"}
    assert response.status_code == 200