import requests

def test_search_user(base_url):
    url = f"{base_url}/users/search?q=john"

    response = requests.get(url, timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert all(
        ("john" in user["firstName"].lower()) or ("john" in user["lastName"].lower())
        for user in data["users"]
    )