import requests

def test_add_product(base_url):
    url = f"{base_url}/products/add"
    payload = {
        "title": "BMW Pencil"
    }

    response = requests.post(url, json=payload, timeout=10)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == "BMW Pencil"
    assert "id" in data