import requests
import pytest

BASE_URL = "https://dummyjson.com"

def test_login_valid():
    url = f"{BASE_URL}/auth/login"

    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30,
    }

    response = requests.post(url, json=payload)
    data = response.json()

    assert response.status_code == 200
    assert "accessToken" in data
    assert "refreshToken" in data

    required_fields = ["id", "username", "email", "firstName", "lastName", "gender", "image"]
    for field in required_fields:
        assert field in data, f"Missing user field: {field}"