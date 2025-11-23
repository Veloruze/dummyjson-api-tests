import pytest

BASE_URL = "https://dummyjson.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL