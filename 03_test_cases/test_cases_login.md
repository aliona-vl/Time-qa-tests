# Test Cases: Login

## Project: Project-Based Time Tracking Web Application

## Test Object

Login functionality for registered users.

## Test Basis

* Registered users can log in with valid credentials.
* Invalid credentials must be rejected.
* Empty required fields must be validated.
* After successful login, the user must be redirected to the correct dashboard according to the user role.
* Unauthorized users must not access protected pages.

---

## Test Conditions

| ID           | Test Condition                               | Priority |
| ------------ | -------------------------------------------- | -------- |
| TCND-LOG-001 | Login with valid credentials                 | High     |
| TCND-LOG-002 | Login with invalid password                  | High     |
| TCND-LOG-003 | Login with unknown email                     | High     |
| TCND-LOG-004 | Validation of empty login fields             | High     |
| TCND-LOG-005 | Correct redirection after login              | High     |
| TCND-LOG-006 | Protection of restricted pages without login | High     |

---

## Test Data

| Data Type              | Example                                           |
| ---------------------- | ------------------------------------------------- |
| Valid manager email    | [manager@test.com](mailto:manager@test.com)       |
| Valid production email | [production@test.com](mailto:production@test.com) |
| Valid password         | TestPassword123!                                  |
| Invalid password       | WrongPassword123                                  |
| Unknown email          | [unknown@test.com](mailto:unknown@test.com)       |
| Empty value            | blank input field                                 |

---

## Test Cases

| Test Case ID | Test Condition                               | Preconditions           | Test Steps                                                                                                   | Test Data                                                          | Expected Result                                                    | Priority | Status  |
| ------------ | -------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | -------- | ------- |
| LOG-001      | Login with valid manager credentials         | Manager user exists     | 1. Open login page. <br> 2. Enter valid manager email. <br> 3. Enter valid password. <br> 4. Click Login.    | [manager@test.com](mailto:manager@test.com) / valid password       | User is logged in and redirected to manager dashboard.             | High     | Not Run |
| LOG-002      | Login with valid production user credentials | Production user exists  | 1. Open login page. <br> 2. Enter valid production email. <br> 3. Enter valid password. <br> 4. Click Login. | [production@test.com](mailto:production@test.com) / valid password | User is logged in and redirected to production dashboard.          | High     | Not Run |
| LOG-003      | Login with wrong password                    | User exists             | 1. Open login page. <br> 2. Enter valid email. <br> 3. Enter wrong password. <br> 4. Click Login.            | valid email / wrong password                                       | Login is rejected and an error message is displayed.               | High     | Not Run |
| LOG-004      | Login with unknown email                     | Login page is available | 1. Open login page. <br> 2. Enter unknown email. <br> 3. Enter any password. <br> 4. Click Login.            | [unknown@test.com](mailto:unknown@test.com)                        | Login is rejected and an error message is displayed.               | High     | Not Run |
| LOG-005      | Login with empty email field                 | Login page is available | 1. Open login page. <br> 2. Leave email field empty. <br> 3. Enter password. <br> 4. Click Login.            | empty email                                                        | Validation message for required email field is displayed.          | High     | Not Run |
| LOG-006      | Login with empty password field              | Login page is available | 1. Open login page. <br> 2. Enter valid email. <br> 3. Leave password field empty. <br> 4. Click Login.      | empty password                                                     | Validation message for required password field is displayed.       | High     | Not Run |
| LOG-007      | Login with empty email and password          | Login page is available | 1. Open login page. <br> 2. Leave email and password empty. <br> 3. Click Login.                             | empty fields                                                       | Validation messages for required fields are displayed.             | High     | Not Run |
| LOG-008      | Login with invalid email format              | Login page is available | 1. Open login page. <br> 2. Enter invalid email format. <br> 3. Enter password. <br> 4. Click Login.         | user.test                                                          | Email validation message is displayed.                             | Medium   | Not Run |
| LOG-009      | Access manager dashboard without login       | User is logged out      | 1. Open manager dashboard URL directly.                                                                      | direct dashboard URL                                               | Access is denied and user is redirected to login page.             | High     | Not Run |
| LOG-010      | Logout and access protected page again       | User is logged in       | 1. Log in. <br> 2. Click Logout. <br> 3. Try to open dashboard again.                                        | valid user                                                         | User is logged out and cannot access protected page without login. | High     | Not Run |

---

## Negative Test Cases

| Test Case ID | Scenario                           | Expected Result                                       |
| ------------ | ---------------------------------- | ----------------------------------------------------- |
| NEG-LOG-001  | User enters wrong password         | Login is rejected.                                    |
| NEG-LOG-002  | User enters unknown email          | Login is rejected.                                    |
| NEG-LOG-003  | User leaves email empty            | Validation message is displayed.                      |
| NEG-LOG-004  | User leaves password empty         | Validation message is displayed.                      |
| NEG-LOG-005  | User opens dashboard without login | User is redirected to login page or access is denied. |

---

## Traceability Matrix

| Requirement ID | Related Acceptance Criteria | Test Case ID                       |
| -------------- | --------------------------- | ---------------------------------- |
| REQ-LOG-001    | AC-LOG-001                  | LOG-001, LOG-002                   |
| REQ-LOG-002    | AC-LOG-002                  | LOG-003                            |
| REQ-LOG-003    | AC-LOG-003                  | LOG-004                            |
| REQ-LOG-004    | AC-LOG-004                  | LOG-005, LOG-006, LOG-007, LOG-008 |
| REQ-LOG-005    | AC-LOG-005                  | LOG-001, LOG-002                   |
| REQ-LOG-006    | AC-LOG-006                  | LOG-009, LOG-010                   |

---

## Notes

Login is a critical function because it controls access to protected application areas.

Special attention should be paid to:

* correct validation of login fields
* secure rejection of invalid credentials
* correct redirection based on user role
* session handling after successful login
* protection of manager and production dashboards from unauthorized access
