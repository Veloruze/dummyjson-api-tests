import requests
import pytest

BASE_URL = "https://dummyjson.com"

def test_access_wrong_token():
    url = f"{BASE_URL}/auth/me"

    headers = {
        "Authorization" : f"Bearer aokwokwokwokwinvalidsiroakwokw"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    assert response.status_code == 401
    assert data["message"] == "Invalid/Expired Token!" 