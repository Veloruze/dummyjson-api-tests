import requests

def test_filter_category(base_url):
    url = f"{base_url}/products/category/smartphones"

    response = requests.get(url)
    data = response.json()

    assert response.status_code == 200
    assert all(
        "smartphones" in product["category"]
        for product in data["products"]
    )