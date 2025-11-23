import requests

def test_delete_user(base_url):
    url = f"{base_url}/users/10"

    response = requests.delete(url, timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert data["isDeleted"] is True