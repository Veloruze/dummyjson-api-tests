import requests

def test_create_new_user(base_url):
    url = f"{base_url}/users/add"

    payload = {
        "firstName": "Ahmad",
        "lastName": "Al Afif",
        "age": 27,
    }

    response = requests.post(url, json=payload)
    data = response.json()

    assert response.status_code == 201

    required_fields = ["id", "firstName", "lastName", "age"]
    for field in required_fields:
        assert field in data, f"Missing user field: {field}"