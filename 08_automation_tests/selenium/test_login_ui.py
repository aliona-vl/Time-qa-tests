```python
"""
UI automation tests for login functionality.

Project: Project-Based Time Tracking Web Application
Tool: PyTest + Selenium WebDriver

Note:
These tests are prepared as automation examples for the QA portfolio.
Selectors may need to be adjusted depending on the final HTML structure of the application.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


BASE_URL = "http://localhost:5000"


def create_driver():
    """
    Creates Chrome WebDriver instance.
    """

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    return driver


def test_login_page_opens():
    """
    Test condition:
    Login page opens successfully.

    Expected result:
    Email field, password field and login button are visible.
    """

    driver = create_driver()

    try:
        driver.get(f"{BASE_URL}/login")

        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        assert email_field.is_displayed()
        assert password_field.is_displayed()
        assert login_button.is_displayed()

    finally:
        driver.quit()


def test_manager_login_successful():
    """
    Test condition:
    Manager logs in with valid credentials.

    Expected result:
    Manager dashboard is displayed after login.
    """

    driver = create_driver()

    try:
        driver.get(f"{BASE_URL}/login")

        driver.find_element(By.NAME, "email").send_keys("manager@test.com")
        driver.find_element(By.NAME, "password").send_keys("TestPassword123!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        assert "dashboard" in driver.current_url.lower()

    finally:
        driver.quit()


def test_login_with_empty_fields_shows_validation():
    """
    Test condition:
    User tries to log in with empty fields.

    Expected result:
    Login should not be successful.
    """

    driver = create_driver()

    try:
        driver.get(f"{BASE_URL}/login")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        assert "login" in driver.current_url.lower()

    finally:
        driver.quit()


def test_production_user_should_not_see_manager_panel_button():
    """
    Test condition:
    Production user logs in and opens production dashboard.

    Expected result:
    Manager Panel button should not be visible for production user.
    """

    driver = create_driver()

    try:
        driver.get(f"{BASE_URL}/login")

        driver.find_element(By.NAME, "email").send_keys("production@test.com")
        driver.find_element(By.NAME, "password").send_keys("TestPassword123!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        page_text = driver.page_source.lower()

        assert "manager panel" not in page_text
        assert "manager-panel" not in page_text

    finally:
        driver.quit()
```
