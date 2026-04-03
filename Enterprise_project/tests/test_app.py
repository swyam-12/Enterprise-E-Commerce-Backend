from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_create_product():
    response = client.post("/products?name=Laptop&price=50000")
    assert response.status_code == 200

def test_create_user():
    response = client.post("/users?username=swyam")
    assert response.status_code == 200

def test_create_order():
    response = client.post("/orders?product_id=1&user_id=1")
    assert response.status_code == 200