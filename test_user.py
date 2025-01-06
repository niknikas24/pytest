import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture
def user_data():
    return {
        "id": 1,
        "username": "jimmy_dale",
        "firstName": "Jimmy",
        "lastName": "Dale",
        "email": "jimmydale@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1,
    }

def test_create_user(user_data):
    response = requests.post(f"{BASE_URL}/user", json=user_data)
    assert response.status_code == 200
    assert response.json()["message"] == str(user_data["id"])

def test_get_user(user_data):
    username = user_data["username"]
    response = requests.get(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["username"] == username

def test_update_user(user_data):
    username = user_data["username"]
    user_data["email"] = "newemail@example.com"
    response = requests.put(f"{BASE_URL}/user/{username}", json=user_data)
    assert response.status_code == 200
# Проверяем, что email обновился
    response = requests.get(f"{BASE_URL}/user/{username}")
    assert response.json()["email"] == "newemail@example.com"

def test_delete_user(user_data):
    username = user_data["username"]
    response = requests.delete(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200
# Проверяем, что пользователь удалён
    response = requests.get(f"{BASE_URL}/user/{username}")
    assert response.status_code == 404

def test_get_non_existent_user():
    response = requests.get(f"{BASE_URL}/user/unknown_user")
    assert response.status_code == 404
