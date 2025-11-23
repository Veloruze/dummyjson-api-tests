import requests


def test_delete_product(base_url):
    url = f"{base_url}/products/10"

    response = requests.delete(url, timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 10
    assert data["isDeleted"] is True