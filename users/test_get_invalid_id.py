import requests
import pytest

BASE_URL = "https://dummyjson.com"

def test_get_invalid_id():
    url = f"{BASE_URL}/users/100500"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 404
    assert data["message"] == "User with id '100500' not found"