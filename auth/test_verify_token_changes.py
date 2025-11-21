import requests
import pytest
import json

BASE_URL = "https://dummyjson.com"

def test_verify_token_changes():
    url = f"{BASE_URL}/auth/login"

    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30,
    }

    token = []

    for i in range(3):
        response = requests.post(url, json=payload)
        data = response.json()

        assert response.status_code == 200
        assert "accessToken" in data
        assert "refreshToken" in data

        token.append({
            "accessToken"   : data["accessToken"],
            "refreshToken"  : data["refreshToken"]
        })

    for i in range(len(token)):
        for j in range(i+1, len(token)):
            assert token[i]["accessToken"] != token[j]["accessToken"]
            assert token[i]["refreshToken"] != token[j]["refreshToken"]