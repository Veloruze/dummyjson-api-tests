import requests

def test_get_all_users(base_url):
    url = f"{base_url}/users"

    response = requests.get(url, timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0