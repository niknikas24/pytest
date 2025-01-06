import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture
def pet_data():
    return {
        "id": 12345,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Reni",
        "photoUrls": ["https://example.com/photo"],
        "tags": [{"id": 1, "name": "tag1"}],
        "status": "available",
    }

def test_create_pet(pet_data):
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == pet_data["name"]
    assert response_data["status"] == pet_data["status"]

def test_get_pet(pet_data):
    pet_id = pet_data["id"]
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == pet_id
    assert response_data["name"] == pet_data["name"]

def test_update_pet_status(pet_data):
    pet_data["status"] = "sold"
    response = requests.put(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "sold"

def test_delete_pet(pet_data):
    pet_id = pet_data["id"]
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
# Проверяем, что питомец удалён
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 404

def test_get_non_existent_pet():
    response = requests.get(f"{BASE_URL}/pet/0")
    assert response.status_code == 404
