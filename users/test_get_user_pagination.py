import requests

def test_get_user_pagination(base_url):
    url = f"{base_url}/users?limit=10&skip=5"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data["skip"] == 5
    assert data["limit"] == 10

