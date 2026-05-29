# Test Cases: Registration with Team Code

## Project: Project-Based Time Tracking Web Application

## Test Object

Registration functionality with and without team code.

## Test Basis

* User can register with a valid team code and join an existing team.
* User can register without team code and work only with personal projects.
* Invalid team code must be rejected.
* Required registration fields must be validated.
* Users from different teams must not access each other’s projects.

---

## Test Conditions

| ID           | Test Condition                                      | Priority |
| ------------ | --------------------------------------------------- | -------- |
| TCND-REG-001 | Registration with valid team code                   | High     |
| TCND-REG-002 | Registration without team code                      | High     |
| TCND-REG-003 | Registration with invalid team code                 | High     |
| TCND-REG-004 | Validation of required fields                       | High     |
| TCND-REG-005 | Data separation between team and personal workspace | High     |

---

## Test Data

| Data Type         | Example                                               |
| ----------------- | ----------------------------------------------------- |
| Valid team code   | TEAM-TEST-001                                         |
| Invalid team code | WRONG-CODE                                            |
| Valid email       | [user.test@example.com](mailto:user.test@example.com) |
| Invalid email     | user.test                                             |
| Valid password    | TestPassword123!                                      |
| Empty value       | blank input field                                     |

---

## Test Cases

| Test Case ID | Test Condition                                             | Preconditions                           | Test Steps                                                                                                                                  | Test Data       | Expected Result                                                                | Priority | Status  |
| ------------ | ---------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------ | -------- | ------- |
| REG-001      | Registration with valid team code                          | Valid team code exists                  | 1. Open registration page. <br> 2. Enter valid user data. <br> 3. Enter valid team code. <br> 4. Click Register.                            | TEAM-TEST-001   | User is registered successfully and assigned to the correct team.              | High     | Not Run |
| REG-002      | Registration without team code                             | Registration page is available          | 1. Open registration page. <br> 2. Enter valid user data. <br> 3. Leave team code field empty. <br> 4. Click Register.                      | Empty team code | User is registered successfully and receives access only to personal projects. | High     | Not Run |
| REG-003      | Registration with invalid team code                        | Registration page is available          | 1. Open registration page. <br> 2. Enter valid user data. <br> 3. Enter invalid team code. <br> 4. Click Register.                          | WRONG-CODE      | Registration is rejected and an error message is displayed.                    | High     | Not Run |
| REG-004      | Registration with empty required fields                    | Registration page is available          | 1. Open registration page. <br> 2. Leave required fields empty. <br> 3. Click Register.                                                     | Empty fields    | Validation messages are displayed for required fields.                         | High     | Not Run |
| REG-005      | Registration with invalid email format                     | Registration page is available          | 1. Open registration page. <br> 2. Enter invalid email format. <br> 3. Fill other required fields correctly. <br> 4. Click Register.        | user.test       | Email validation message is displayed.                                         | Medium   | Not Run |
| REG-006      | Registration with already used email                       | User with the same email already exists | 1. Open registration page. <br> 2. Enter an already registered email. <br> 3. Fill other required fields correctly. <br> 4. Click Register. | existing email  | Registration is rejected and message about existing user is displayed.         | High     | Not Run |
| REG-007      | Team user can see team projects after registration         | User registered with valid team code    | 1. Register with valid team code. <br> 2. Log in. <br> 3. Open dashboard.                                                                   | TEAM-TEST-001   | User can see projects assigned to the team according to role permissions.      | High     | Not Run |
| REG-008      | Personal user cannot see team projects                     | User registered without team code       | 1. Register without team code. <br> 2. Log in. <br> 3. Open dashboard.                                                                      | Empty team code | User sees only personal workspace and cannot access team projects.             | High     | Not Run |
| REG-009      | User from another team cannot access foreign team projects | Two different teams exist               | 1. Register user in Team A. <br> 2. Register another user in Team B. <br> 3. Try to access Team B project as Team A user.                   | Team A / Team B | Access is denied. User cannot see or open projects from another team.          | High     | Not Run |
| REG-010      | Password field validation                                  | Registration page is available          | 1. Open registration page. <br> 2. Enter password that does not meet requirements. <br> 3. Click Register.                                  | weak password   | Password validation message is displayed.                                      | Medium   | Not Run |

---

## Negative Test Cases

| Test Case ID | Scenario                                    | Expected Result                                                  |
| ------------ | ------------------------------------------- | ---------------------------------------------------------------- |
| NEG-REG-001  | Invalid team code is entered                | User is not assigned to any team and error message is displayed. |
| NEG-REG-002  | Required fields are empty                   | Registration is not completed. Validation messages are shown.    |
| NEG-REG-003  | Email format is invalid                     | Registration is blocked. Email validation message is shown.      |
| NEG-REG-004  | Already registered email is used            | Registration is rejected. Existing user message is displayed.    |
| NEG-REG-005  | User tries to access another team’s project | Access is denied.                                                |

---

## Traceability Matrix

| Requirement ID | Related Acceptance Criteria | Test Case ID              |
| -------------- | --------------------------- | ------------------------- |
| REQ-REG-001    | AC-REG-001                  | REG-001                   |
| REQ-REG-002    | AC-REG-003                  | REG-002                   |
| REQ-REG-003    | AC-REG-004                  | REG-003                   |
| REQ-REG-004    | AC-REG-005                  | REG-004, REG-005, REG-010 |
| REQ-REG-005    | AC-REG-006                  | REG-008, REG-009          |

---

## Notes

This functionality is business-critical because the team code controls access to shared project data. Incorrect team assignment or missing data separation can lead to unauthorized access to project information.

Special attention should be paid to:

* valid and invalid team code handling
* separation between team and personal workspace
* validation of required fields
* prevention of unauthorized access to other teams
* correct dashboard after registration
