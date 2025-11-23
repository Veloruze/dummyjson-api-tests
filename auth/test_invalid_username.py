import requests

def test_invalid_username(base_url):
    url = f"{base_url}/auth/login"

    payload = {
        "username": "veloruze",
        "password": "emilyspass",
        "expiresInMins": 30,
    }

    response = requests.post(url, json=payload)
    data = response.json()

    assert response.status_code == 400
    assert data["message"] == "Invalid credentials"