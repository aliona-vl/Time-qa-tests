# Automation Test Strategy

## Project: Project-Based Time Tracking Web Application

## Purpose

This document describes the planned automation testing approach for the project-based time tracking web application.

The goal of automation testing is to support repeated testing of critical workflows such as login, project creation, time tracking and role-based access.

Automation does not replace manual testing. It supports regression testing by checking stable and business-critical functionality faster and more consistently.

---

## 1. Automation Scope

The first automation focus should be on stable and repeatable test scenarios.

Recommended areas for automation:

* login with valid and invalid credentials
* registration validation
* project creation
* start/stop time tracking
* prevention of overlapping time entries
* role-based access checks
* QR access validation
* report availability after project completion

---

## 2. Out of Scope for Initial Automation

The following areas are not recommended for initial automation:

* unstable UI elements that change often
* visual design details
* complex report layout checks
* manual exploratory testing
* usability testing
* tests requiring real external users
* long-running QR expiration tests without test configuration

These can be added later after the application becomes more stable.

---

## 3. Automation Tools

| Area                 | Tool               |
| -------------------- | ------------------ |
| Programming language | Python             |
| Test framework       | PyTest             |
| UI automation        | Selenium WebDriver |
| API testing          | Requests / Postman |
| Browser              | Google Chrome      |
| Version control      | Git / GitHub       |
| Test documentation   | Markdown           |

---

## 4. Suggested Automation Folder Structure

```text
08_automation_tests/
│
├── automation_test_strategy.md
│
├── pytest/
│   ├── test_login_api.py
│   ├── test_registration_api.py
│   ├── test_project_api.py
│   └── test_time_tracking_api.py
│
└── selenium/
    ├── test_login_ui.py
    ├── test_manager_dashboard_ui.py
    ├── test_project_creation_ui.py
    └── test_time_tracking_ui.py
```

---

## 5. Automation Priorities

| Priority | Area                         | Reason                                     |
| -------- | ---------------------------- | ------------------------------------------ |
| High     | Login                        | Basic access to the application            |
| High     | Role-based access            | Prevents unauthorized access               |
| High     | Time tracking                | Core business function                     |
| High     | Overlapping timer prevention | Protects report accuracy                   |
| High     | Report availability          | Prevents incomplete final reports          |
| Medium   | Project creation             | Important business workflow                |
| Medium   | QR access                    | Important but may require test token setup |
| Low      | UI layout                    | Better tested manually at the beginning    |

---

## 6. API Automation Candidates

API automation is useful for testing business logic directly.

Recommended API tests:

| Test ID      | Scenario                               | Expected Result   |
| ------------ | -------------------------------------- | ----------------- |
| AUTO-API-001 | Login with valid credentials           | Status 200        |
| AUTO-API-002 | Login with invalid password            | Status 401        |
| AUTO-API-003 | Create project with valid data         | Status 201        |
| AUTO-API-004 | Create project without project name    | Status 400        |
| AUTO-API-005 | Start timer with valid data            | Status 201        |
| AUTO-API-006 | Start timer without activity           | Status 400        |
| AUTO-API-007 | Start overlapping timer                | Status 409        |
| AUTO-API-008 | Get report for active project          | Status 409 or 403 |
| AUTO-API-009 | Production user opens manager endpoint | Status 403        |
| AUTO-API-010 | Expired QR token is rejected           | Status 403        |

---

## 7. UI Automation Candidates

UI automation is useful for checking critical user workflows through the browser.

Recommended UI tests:

| Test ID     | Scenario                                                 | Expected Result                            |
| ----------- | -------------------------------------------------------- | ------------------------------------------ |
| AUTO-UI-001 | Login page opens                                         | Login form is visible                      |
| AUTO-UI-002 | Manager logs in successfully                             | Manager dashboard is displayed             |
| AUTO-UI-003 | Production user logs in successfully                     | Production dashboard is displayed          |
| AUTO-UI-004 | Manager creates project                                  | New project appears on dashboard           |
| AUTO-UI-005 | User starts time tracking                                | Active timer is displayed                  |
| AUTO-UI-006 | User stops time tracking                                 | Time entry is saved                        |
| AUTO-UI-007 | Production user cannot see Manager Panel button          | Manager Panel button is not visible        |
| AUTO-UI-008 | Report button is available only after project completion | Report is not available for active project |

---

## 8. Example PyTest API Test

Example file:

```text
08_automation_tests/pytest/test_login_api.py
```

Example test:

```python
import requests

BASE_URL = "http://localhost:5000"

def test_login_with_invalid_password():
    payload = {
        "email": "manager@test.com",
        "password": "WrongPassword123"
    }

    response = requests.post(f"{BASE_URL}/api/login", json=payload)

    assert response.status_code in [400, 401]
```

---

## 9. Example Selenium UI Test

Example file:

```text
08_automation_tests/selenium/test_login_ui.py
```

Example test:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_login_page_opens():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000/login")

    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")

    assert email_field.is_displayed()
    assert password_field.is_displayed()

    driver.quit()
```

---

## 10. Test Data for Automation

Automation tests should use separate test data.

Recommended test data:

| Data             | Example                                           |
| ---------------- | ------------------------------------------------- |
| Manager user     | [manager@test.com](mailto:manager@test.com)       |
| Production user  | [production@test.com](mailto:production@test.com) |
| Invalid password | WrongPassword123                                  |
| Test project     | Automated Test Project                            |
| Activity         | Fertigung                                         |
| Employee         | Max Tester                                        |
| Team code        | TEAM-TEST-001                                     |

Test data should be reset before or after automated test execution.

---

## 11. Automation Risks

| Risk                                  | Impact                       | Mitigation                                        |
| ------------------------------------- | ---------------------------- | ------------------------------------------------- |
| UI elements change often              | Selenium tests may fail      | Use stable selectors and data attributes          |
| Test data is not reset                | Tests may become unreliable  | Prepare clean test data                           |
| API endpoints are not stable          | API tests may fail           | Start with planned API tests                      |
| QR expiration takes too long          | Tests are slow               | Use test configuration with short expiration time |
| Reports depend on previous test steps | Test results may be unstable | Prepare known test entries before report test     |

---

## 12. Best Practices

Recommended automation practices:

* start with small and stable test cases
* use clear test names
* separate API tests and UI tests
* do not automate everything immediately
* keep manual exploratory testing
* use test data that can be repeated
* avoid depending on random existing data
* document what is automated and what is manual

---

## 13. Automation Summary

Automation testing should focus first on the most important business risks:

* login
* role-based access
* time tracking
* prevention of overlapping time entries
* QR access validation
* report generation rules

The automation suite can be expanded step by step after the manual test documentation is complete and stable.
