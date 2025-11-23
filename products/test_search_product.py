import requests

def test_search_product(base_url):
    url = f"{base_url}/products/search?q=phone"

    response = requests.get(url, timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert all(
        ("phone" in product["title"].lower() or "phone" in product["description"].lower())
        for product in data["products"]
    )