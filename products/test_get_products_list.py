import requests

def test_get_products_list(base_url):
    url = f"{base_url}/products"

    response = requests.get(url, timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0