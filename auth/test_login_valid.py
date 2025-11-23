import requests

def test_login_valid(base_url):
    url = f"{base_url}/auth/login"

    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30,
    }

    response = requests.post(url, json=payload)
    data = response.json()

    assert response.status_code == 200
    assert "accessToken" in data
    assert "refreshToken" in data

    required_fields = ["id", "username", "email", "firstName", "lastName", "gender", "image"]
    for field in required_fields:
        assert field in data, f"Missing user field: {field}"