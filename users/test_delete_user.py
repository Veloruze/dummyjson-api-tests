import requests
import pytest
import json

BASE_URL = "https://dummyjson.com"

def test_delete_user():
    url = f"{BASE_URL}/users/10"

    response = requests.delete(url)
    data = response.json()

    assert response.status_code == 200
    assert data["isDeleted"] == True