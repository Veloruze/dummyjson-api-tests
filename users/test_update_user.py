import requests
import pytest

BASE_URL = "https://dummyjson.com"

def test_update_user():
    url = f"{BASE_URL}/users/10"

    payload = {
        "lastName": "Al Afif",
        "company" : {
        "title": "CEO"
        }
    }

    response = requests.put(url, json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["lastName"] == "Al Afif"
    assert data["company"]["title"].lower() == "ceo"

