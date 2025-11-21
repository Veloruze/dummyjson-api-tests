import requests
import pytest
import json

BASE_URL = "https://dummyjson.com"

def test_search_user():
    url = f"{BASE_URL}/users/search?q=john"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 200
    assert any(
        ("john" in user["firstName"].lower()) or ("john" in user["lastName"].lower())
        for user in data["users"]
    )