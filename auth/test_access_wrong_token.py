import requests

def test_access_wrong_token(base_url):
    url = f"{base_url}/auth/me"

    headers = {
        "Authorization" : f"Bearer aokwokwokwokwinvalidsiroakwokw"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    assert response.status_code == 401
    assert data["message"] == "Invalid/Expired Token!" 