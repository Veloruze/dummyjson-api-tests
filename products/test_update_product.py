import requests

def test_update_product(base_url):
    url = f"{base_url}/products/10"
    payload = {
        "title": "iPhone Galaxy +"
    }

    response = requests.put(url, json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 10
    assert data["title"] == "iPhone Galaxy +"