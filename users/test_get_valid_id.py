import requests

def test_get_valid_id(base_url):
    url = f"{base_url}/users/1"

    response = requests.get(url, timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    required_fields = ["id", "firstName", "lastName", "age"]
    for field in required_fields:
        assert field in data