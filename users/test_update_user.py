import requests

def test_update_user(base_url):
    url = f"{base_url}/users/10"

    payload = {
        "lastName": "Al Afif",
        "company" : {
            "title": "CEO"
        }
    }

    response = requests.put(url, json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["lastName"] == "Al Afif"
    assert data["company"]["title"].lower() == "ceo"

