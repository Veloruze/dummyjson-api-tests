import requests

def test_get_invalid_id(base_url):
    url = f"{base_url}/users/1005"

    response = requests.get(url, timeout=10)
    data = response.json()

    assert response.status_code == 404
    assert data["message"] == "User with id '1005' not found"