import requests
import pytest

BASE_URL = "https://dummyjson.com"

def test_invalid_password():
    url = f"{BASE_URL}/auth/login"

    payload = {
        "username": "emilys",
        "password": "invalidpass",
        "expiresInMins": 30,
    }

    response = requests.post(url, json=payload)
    data = response.json()
    assert response.status_code == 400
    assert data["message"] == "Invalid credentials"