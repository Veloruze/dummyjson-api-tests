import requests

def test_create_new_user(base_url):
    url = f"{base_url}/users/add"

    payload = {
        "firstName": "Ahmad",
        "lastName": "Al Afif",
        "age": 27,
    }

    response = requests.post(url, json=payload, timeout=10)
    data = response.json()

    assert response.status_code == 201
    assert "id" in data
    
    assert data["firstName"] == payload["firstName"]
    assert data["lastName"] == payload["lastName"]
    assert data["age"] == payload["age"]