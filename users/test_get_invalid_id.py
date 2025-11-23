import requests

def test_get_invalid_id(base_url):
    url = f"{base_url}/users/100500"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 404
    assert data["message"] == "User with id '100500' not found"