import requests

def test_invalid_password(base_url):
    url = f"{base_url}/auth/login"

    payload = {
        "username": "emilys",
        "password": "invalidpass",
        "expiresInMins": 30,
    }

    response = requests.post(url, json=payload, timeout=10)
    data = response.json()
    assert response.status_code == 400
    assert data["message"] == "Invalid credentials"