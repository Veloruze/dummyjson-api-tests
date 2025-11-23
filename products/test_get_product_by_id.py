import requests

def test_get_product_by_id(base_url):
    url = f"{base_url}/products/10"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 10