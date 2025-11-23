import requests

def test_get_product_invalid_id(base_url):
    url = f"{base_url}products/1005"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 404
    assert data["message"] == "Product with id '1005' not found"