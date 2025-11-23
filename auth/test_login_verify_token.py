import requests

def test_login_verify_token(base_url):
    loginUrl = f"{base_url}/auth/login"

    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30,
    }

    response = requests.post(loginUrl, json=payload)
    logindata = response.json()

    me_url = f"{base_url}/auth/me"
    headers = {
        "Authorization" : f"Bearer {logindata["accessToken"]}"
    }

    me_response = requests.get(me_url, headers=headers)
    me_data = me_response.json()

    assert response.status_code == 200
    required_fields = ["id", "username", "email", "firstName", "lastName", "gender", "image"]
    for field in required_fields:
        assert field in me_data, f"Missing user field: {field}"