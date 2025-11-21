import requests
import pytest

BASE_URL = "https://dummyjson.com"

def test_get_user_pagination():
    url = f"{BASE_URL}/users?limit=10&skip=5"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data["skip"] == 5
    assert data["limit"] == 10

