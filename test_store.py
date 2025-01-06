import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture
def order_data():
    return {
        "id": 98765,
        "petId": 12345,
        "quantity": 1,
        "shipDate": "2025-01-06T08:00:00.000Z",
        "status": "placed",
        "complete": False,
    }

def test_create_order(order_data):
    response = requests.post(f"{BASE_URL}/store/order", json=order_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "placed"

def test_get_order(order_data):
    order_id = order_data["id"]
    response = requests.get(f"{BASE_URL}/store/order/{order_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == order_id

def test_delete_order(order_data):
    order_id = order_data["id"]
    response = requests.delete(f"{BASE_URL}/store/order/{order_id}")
    assert response.status_code == 200
# Проверяем, что заказ удален
    response = requests.get(f"{BASE_URL}/store/order/{order_id}")
    assert response.status_code == 404

def test_get_non_existent_order():
    response = requests.get(f"{BASE_URL}/store/order/0")
    assert response.status_code == 404

def test_create_order_invalid_data():
    invalid_order_data = {
        "id": "invalid_id",
        "petId": "invalid_petId",
        "quantity": -1,
        "status": "unknown",
    }
    response = requests.post(f"{BASE_URL}/store/order", json=invalid_order_data)
    assert response.status_code == 500
