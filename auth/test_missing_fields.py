import requests

def test_missing_fields(base_url):
    url = f"{base_url}/auth/login"

    payload = {
        "username": "veloruze",
        "expiresInMins": 30
    }

    response = requests.post(url, json=payload)
    data = response.json()

    assert response.status_code == 400
    assert data["message"] == "Username and password required"

