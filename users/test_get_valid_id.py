import requests
import pytest

BASE_URL = "https://dummyjson.com"

def test_get_valid_id():
    url = f"{BASE_URL}/users/1"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1