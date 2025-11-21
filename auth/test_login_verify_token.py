import requests
import pytest

BASE_URL = "https://dummyjson.com"

def test_login_verify_token():
    loginUrl = f"{BASE_URL}/auth/login"

    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30,
    }

    response = requests.post(loginUrl, json=payload)
    logindata = response.json()

    me_url = f"{BASE_URL}/auth/me"
    headers = {
        "Authorization" : f"Bearer {logindata["accessToken"]}"
    }

    me_response = requests.get(me_url, headers=headers)
    me_data = me_response.json()

    assert response.status_code == 200
    required_fields = ["id", "username", "email", "firstName", "lastName", "gender", "image"]
    for field in required_fields:
        assert field in me_data, f"Missing user field: {field}"