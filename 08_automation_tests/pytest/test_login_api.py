```python
"""
API tests for login functionality.

Project: Project-Based Time Tracking Web Application
Tool: PyTest + requests

Note:
These tests are prepared as automation examples for the QA portfolio.
The endpoint URL and response structure may need to be adjusted depending on the final backend implementation.
"""

import requests


BASE_URL = "http://localhost:5000"


def test_login_with_valid_manager_credentials():
    """
    Test condition:
    Manager can log in with valid credentials.

    Expected result:
    API returns status code 200 and successful login response.
    """

    payload = {
        "email": "manager@test.com",
        "password": "TestPassword123!"
    }

    response = requests.post(f"{BASE_URL}/api/login", json=payload)

    assert response.status_code == 200


def test_login_with_invalid_password():
    """
    Test condition:
    Login with wrong password is rejected.

    Expected result:
    API returns 400 or 401 status code.
    """

    payload = {
        "email": "manager@test.com",
        "password": "WrongPassword123"
    }

    response = requests.post(f"{BASE_URL}/api/login", json=payload)

    assert response.status_code in [400, 401]


def test_login_with_unknown_email():
    """
    Test condition:
    Login with unknown email is rejected.

    Expected result:
    API returns 400 or 401 status code.
    """

    payload = {
        "email": "unknown@test.com",
        "password": "TestPassword123!"
    }

    response = requests.post(f"{BASE_URL}/api/login", json=payload)

    assert response.status_code in [400, 401]


def test_login_with_empty_email():
    """
    Test condition:
    Login without email is rejected.

    Expected result:
    API returns 400 status code.
    """

    payload = {
        "email": "",
        "password": "TestPassword123!"
    }

    response = requests.post(f"{BASE_URL}/api/login", json=payload)

    assert response.status_code == 400


def test_login_with_empty_password():
    """
    Test condition:
    Login without password is rejected.

    Expected result:
    API returns 400 status code.
    """

    payload = {
        "email": "manager@test.com",
        "password": ""
    }

    response = requests.post(f"{BASE_URL}/api/login", json=payload)

    assert response.status_code == 400


def test_login_with_empty_request_body():
    """
    Test condition:
    Login request without required data is rejected.

    Expected result:
    API returns 400 status code.
    """

    payload = {}

    response = requests.post(f"{BASE_URL}/api/login", json=payload)

    assert response.status_code == 400
```
