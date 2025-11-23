# DummyJSON API Tests

API automation testing for [DummyJSON](https://dummyjson.com/) endpoints using Python and pytest.

## Project Structure

```
dummyjson-api-tests/
├── conftest.py          # Shared fixtures
├── requirements.txt     # Dependencies
├── auth/                # Authentication tests
│   ├── test_login_valid.py
│   ├── test_login_verify_token.py
│   ├── test_invalid_password.py
│   ├── test_invalid_username.py
│   ├── test_missing_fields.py
│   └── test_access_wrong_token.py
├── users/               # Users API tests
│   ├── test_get_all_users.py
│   ├── test_get_valid_id.py
│   ├── test_get_invalid_id.py
│   ├── test_create_new_user.py
│   ├── test_update_user.py
│   ├── test_delete_user.py
│   ├── test_get_user_pagination.py
│   └── test_search_user.py
└── products/            # Products API tests
    ├── test_get_products_list.py
    ├── test_get_product_by_id.py
    ├── test_get_product_invalid_id.py
    ├── test_search_product.py
    ├── test_filter_category.py
    ├── test_add_product.py
    ├── test_update_product.py
    ├── test_delete_product.py
    └── test_product_pagination_and_limit.py
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/Veloruze/dummyjson-api-tests.git
cd dummyjson-api-tests
```

2. Create virtual environment (optional)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:
```bash
pytest
```

Run specific folder:
```bash
pytest auth/
pytest users/
pytest products/
```

Run single test file:
```bash
pytest auth/test_login_valid.py
```

Run with verbose output:
```bash
pytest -v
```

Run with timeout (recommended):
```bash
pip install pytest-timeout
pytest --timeout=15
```

## Test Coverage

| Module | Endpoint | Tests |
|--------|----------|-------|
| Auth | POST /auth/login | Valid login, invalid password, invalid username, missing fields |
| Auth | GET /auth/me | Verify token, wrong token |
| Users | GET /users | Get all, pagination, search |
| Users | GET /users/:id | Valid ID, invalid ID |
| Users | POST /users/add | Create new user |
| Users | PUT /users/:id | Update user |
| Users | DELETE /users/:id | Delete user |
| Products | GET /products | Get all, pagination, search, filter by category |
| Products | GET /products/:id | Valid ID, invalid ID |
| Products | POST /products/add | Add product |
| Products | PUT /products/:id | Update product |
| Products | DELETE /products/:id | Delete product |

## Tech Stack

- Python 3.x
- pytest
- requests
