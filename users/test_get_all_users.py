import requests
import pytest

BASE_URL = "https://dummyjson.com"

def test_get_all_users():
    url = f"{BASE_URL}/users"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 200
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0