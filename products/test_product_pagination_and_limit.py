import requests

def test_product_pagination_and_limit(base_url):
    url = f"{base_url}/products?limit=5&skip=10"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data["skip"] == 10
    assert data["limit"] == 5