# API Test Cases

## Project: Project-Based Time Tracking Web Application

## Purpose

This document describes possible API test cases for the project-based time tracking application.

The goal of API testing is to verify that backend endpoints return correct responses, validate input data, protect restricted resources and save project-related data correctly.

> Note: These API test cases are prepared as a QA portfolio example and can be extended when stable API endpoints are available in the test environment.

---

## 1. API Testing Scope

API testing should cover the following areas:

* user registration
* login
* team code validation
* project creation
* project list retrieval
* start time tracking
* stop time tracking
* manual time entry
* QR access validation
* project completion
* report generation
* role-based access control

---

## 2. API Test Environment

| Area           | Value                                                             |
| -------------- | ----------------------------------------------------------------- |
| Application    | Project-Based Time Tracking Web Application                       |
| Backend        | Python / Flask                                                    |
| Database       | PostgreSQL                                                        |
| API tool       | Postman                                                           |
| Test type      | API functional testing                                            |
| Data format    | JSON                                                              |
| Authentication | Session / token-based authentication, depending on implementation |

---

## 3. General API Test Conditions

| ID           | Test Condition                            | Priority |
| ------------ | ----------------------------------------- | -------- |
| API-COND-001 | API accepts valid request data            | High     |
| API-COND-002 | API rejects invalid request data          | High     |
| API-COND-003 | API returns correct HTTP status codes     | High     |
| API-COND-004 | API protects restricted endpoints         | High     |
| API-COND-005 | API saves data correctly in the database  | High     |
| API-COND-006 | API does not return data from other teams | High     |

---

# 4. Registration API

## Endpoint

```text
POST /api/register
```

## Description

Registers a new user with or without team code.

## Test Cases

| Test Case ID | Scenario                            | Request Data                        | Expected Status | Expected Result                              | Priority |
| ------------ | ----------------------------------- | ----------------------------------- | --------------- | -------------------------------------------- | -------- |
| API-REG-001  | Register with valid team code       | valid user data + valid team code   | 201 Created     | User is created and assigned to correct team | High     |
| API-REG-002  | Register without team code          | valid user data, empty team code    | 201 Created     | User is created with personal workspace      | High     |
| API-REG-003  | Register with invalid team code     | valid user data + invalid team code | 400 Bad Request | Error message is returned                    | High     |
| API-REG-004  | Register with empty required fields | missing email/password              | 400 Bad Request | Validation errors are returned               | High     |
| API-REG-005  | Register with existing email        | already registered email            | 409 Conflict    | Existing user error is returned              | High     |
| API-REG-006  | Register with invalid email format  | invalid email                       | 400 Bad Request | Email validation error is returned           | Medium   |

## Example Request

```json
{
  "email": "new.user@test.com",
  "password": "TestPassword123!",
  "teamCode": "TEAM-TEST-001"
}
```

## Example Expected Response

```json
{
  "message": "User registered successfully",
  "workspaceType": "team"
}
```

---

# 5. Login API

## Endpoint

```text
POST /api/login
```

## Description

Authenticates user and starts a session or returns an access token.

## Test Cases

| Test Case ID | Scenario                                | Request Data                | Expected Status  | Expected Result                              | Priority |
| ------------ | --------------------------------------- | --------------------------- | ---------------- | -------------------------------------------- | -------- |
| API-LOG-001  | Login with valid manager credentials    | valid email/password        | 200 OK           | Login successful, manager access returned    | High     |
| API-LOG-002  | Login with valid production credentials | valid email/password        | 200 OK           | Login successful, production access returned | High     |
| API-LOG-003  | Login with wrong password               | valid email, wrong password | 401 Unauthorized | Login rejected                               | High     |
| API-LOG-004  | Login with unknown email                | unknown email               | 401 Unauthorized | Login rejected                               | High     |
| API-LOG-005  | Login with empty fields                 | empty email/password        | 400 Bad Request  | Validation error returned                    | High     |

## Example Request

```json
{
  "email": "manager@test.com",
  "password": "TestPassword123!"
}
```

## Example Expected Response

```json
{
  "message": "Login successful",
  "role": "manager"
}
```

---

# 6. Project API

## Endpoint

```text
POST /api/projects
```

## Description

Creates a new project.

## Test Cases

| Test Case ID | Scenario                         | Request Data         | Expected Status | Expected Result                                   | Priority |
| ------------ | -------------------------------- | -------------------- | --------------- | ------------------------------------------------- | -------- |
| API-PROJ-001 | Create project with valid data   | valid project data   | 201 Created     | Project is created                                | High     |
| API-PROJ-002 | Create project without name      | missing project name | 400 Bad Request | Validation error returned                         | High     |
| API-PROJ-003 | Create project without customer  | missing customer     | 400 Bad Request | Validation error returned if customer is required | Medium   |
| API-PROJ-004 | Production user creates project  | production user auth | 403 Forbidden   | Access denied                                     | High     |
| API-PROJ-005 | Project assigned to correct team | manager Team A auth  | 201 Created     | Project belongs to Team A only                    | High     |

## Example Request

```json
{
  "projectName": "Test Project A",
  "customer": "Testkunde Müller GmbH",
  "status": "active"
}
```

---

## Endpoint

```text
GET /api/projects
```

## Description

Returns projects visible to the current user.

## Test Cases

| Test Case ID | Scenario                                | Authentication                   | Expected Status  | Expected Result                     | Priority |
| ------------ | --------------------------------------- | -------------------------------- | ---------------- | ----------------------------------- | -------- |
| API-PROJ-006 | Manager gets team projects              | manager Team A                   | 200 OK           | Only Team A projects are returned   | High     |
| API-PROJ-007 | Personal user gets personal projects    | personal user                    | 200 OK           | Only personal projects are returned | High     |
| API-PROJ-008 | User tries to get another team projects | Team A user requests Team B data | 403 Forbidden    | Access denied                       | High     |
| API-PROJ-009 | Unauthorized user requests projects     | no authentication                | 401 Unauthorized | Access denied                       | High     |

---

# 7. Start Time Tracking API

## Endpoint

```text
POST /api/time/start
```

## Description

Starts time tracking for selected project, activity and employee.

## Test Cases

| Test Case ID | Scenario                                | Request Data                | Expected Status | Expected Result                    | Priority |
| ------------ | --------------------------------------- | --------------------------- | --------------- | ---------------------------------- | -------- |
| API-TIME-001 | Start timer with valid data             | project, activity, employee | 201 Created     | Timer starts successfully          | High     |
| API-TIME-002 | Start timer without activity            | missing activity            | 400 Bad Request | Validation error returned          | High     |
| API-TIME-003 | Start timer without employee            | missing employee            | 400 Bad Request | Validation error returned          | High     |
| API-TIME-004 | Start timer without project             | missing project             | 400 Bad Request | Validation error returned          | High     |
| API-TIME-005 | Start second timer for same employee    | active timer already exists | 409 Conflict    | Overlapping time entry is rejected | High     |
| API-TIME-006 | Production user starts allowed task     | production user auth        | 201 Created     | Timer starts for assigned task     | High     |
| API-TIME-007 | Installer starts timer through valid QR | valid QR token              | 201 Created     | Installer timer starts             | High     |

## Example Request

```json
{
  "projectId": 1,
  "activity": "Fertigung",
  "employeeId": 2
}
```

---

# 8. Stop Time Tracking API

## Endpoint

```text
POST /api/time/stop
```

## Description

Stops an active timer and saves duration.

## Test Cases

| Test Case ID | Scenario                        | Request Data                 | Expected Status | Expected Result                   | Priority |
| ------------ | ------------------------------- | ---------------------------- | --------------- | --------------------------------- | -------- |
| API-TIME-008 | Stop active timer               | active timer ID              | 200 OK          | Timer stops and duration is saved | High     |
| API-TIME-009 | Stop non-existing timer         | invalid timer ID             | 404 Not Found   | Error message returned            | Medium   |
| API-TIME-010 | Stop already stopped timer      | stopped timer ID             | 409 Conflict    | Duplicate stop is rejected        | High     |
| API-TIME-011 | Stop timer by unauthorized user | timer from another team/user | 403 Forbidden   | Access denied                     | High     |

## Example Request

```json
{
  "timeEntryId": 25
}
```

---

# 9. Manual Time Entry API

## Endpoint

```text
POST /api/time/manual
```

## Description

Creates a manual time entry.

## Test Cases

| Test Case ID | Scenario                              | Request Data                                      | Expected Status | Expected Result           | Priority |
| ------------ | ------------------------------------- | ------------------------------------------------- | --------------- | ------------------------- | -------- |
| API-MAN-001  | Create manual entry with valid data   | valid project, employee, activity, start/end time | 201 Created     | Manual entry is saved     | Medium   |
| API-MAN-002  | End time before start time            | invalid time range                                | 400 Bad Request | Entry is rejected         | High     |
| API-MAN-003  | Missing employee                      | no employee                                       | 400 Bad Request | Validation error returned | Medium   |
| API-MAN-004  | Missing activity                      | no activity                                       | 400 Bad Request | Validation error returned | Medium   |
| API-MAN-005  | Manual entry for another team project | unauthorized project                              | 403 Forbidden   | Access denied             | High     |

---

# 10. QR Access API

## Endpoint

```text
POST /api/qr/generate
```

## Description

Generates QR access for production users or installers.

## Test Cases

| Test Case ID | Scenario                             | Request Data                | Expected Status | Expected Result                 | Priority |
| ------------ | ------------------------------------ | --------------------------- | --------------- | ------------------------------- | -------- |
| API-QR-001   | Manager generates installer QR       | project ID, installer type  | 201 Created     | Temporary QR token is generated | High     |
| API-QR-002   | Manager generates production QR      | project ID, production type | 201 Created     | Long-term QR token is generated | High     |
| API-QR-003   | Production user generates QR         | production user auth        | 403 Forbidden   | Access denied                   | High     |
| API-QR-004   | Generate QR for non-existing project | invalid project ID          | 404 Not Found   | Error returned                  | Medium   |
| API-QR-005   | Generate QR for another team project | unauthorized project        | 403 Forbidden   | Access denied                   | High     |

---

## Endpoint

```text
GET /api/qr/validate/{token}
```

## Description

Validates QR access token.

## Test Cases

| Test Case ID | Scenario                      | Token             | Expected Status               | Expected Result | Priority |
| ------------ | ----------------------------- | ----------------- | ----------------------------- | --------------- | -------- |
| API-QR-006   | Validate valid installer QR   | valid token       | 200 OK                        | Access allowed  | High     |
| API-QR-007   | Validate expired installer QR | expired token     | 403 Forbidden                 | Access denied   | High     |
| API-QR-008   | Validate invalid QR token     | invalid token     | 404 Not Found                 | Access denied   | High     |
| API-QR-009   | Validate modified QR token    | manipulated token | 403 Forbidden / 404 Not Found | Access denied   | High     |

---

# 11. Project Completion API

## Endpoint

```text
POST /api/projects/{projectId}/complete
```

## Description

Marks project as completed.

## Test Cases

| Test Case ID | Scenario                           | Authentication                    | Expected Status       | Expected Result                     | Priority |
| ------------ | ---------------------------------- | --------------------------------- | --------------------- | ----------------------------------- | -------- |
| API-COMP-001 | Manager completes active project   | manager                           | 200 OK                | Project status changes to completed | High     |
| API-COMP-002 | Production user completes project  | production user                   | 403 Forbidden         | Access denied                       | High     |
| API-COMP-003 | Complete another team project      | manager Team A for Team B project | 403 Forbidden         | Access denied                       | High     |
| API-COMP-004 | Complete non-existing project      | manager                           | 404 Not Found         | Error returned                      | Medium   |
| API-COMP-005 | Complete already completed project | manager                           | 409 Conflict / 200 OK | No duplicate completion issue       | Medium   |

---

# 12. Report API

## Endpoint

```text
GET /api/reports/{projectId}
```

## Description

Returns final report for completed project.

## Test Cases

| Test Case ID | Scenario                            | Authentication                         | Expected Status              | Expected Result              | Priority |
| ------------ | ----------------------------------- | -------------------------------------- | ---------------------------- | ---------------------------- | -------- |
| API-REP-001  | Get report for completed project    | manager                                | 200 OK                       | Report data returned         | High     |
| API-REP-002  | Get report for active project       | manager                                | 409 Conflict / 403 Forbidden | Report generation blocked    | High     |
| API-REP-003  | Production user requests report     | production user                        | 403 Forbidden                | Access denied                | High     |
| API-REP-004  | Installer requests report           | QR user                                | 403 Forbidden                | Access denied                | High     |
| API-REP-005  | Get report for another team project | Team A manager requests Team B project | 403 Forbidden                | Access denied                | High     |
| API-REP-006  | Report includes total time          | completed project                      | 200 OK                       | Total time is correct        | High     |
| API-REP-007  | Report includes time by employee    | completed project                      | 200 OK                       | Employee grouping is correct | High     |
| API-REP-008  | Report includes time by activity    | completed project                      | 200 OK                       | Activity grouping is correct | High     |

---

# 13. Expected HTTP Status Codes

| Status Code      | Meaning                   | Example                                    |
| ---------------- | ------------------------- | ------------------------------------------ |
| 200 OK           | Request successful        | Login, get report, stop timer              |
| 201 Created      | Resource created          | Register, create project, start timer      |
| 400 Bad Request  | Invalid input             | Missing required fields                    |
| 401 Unauthorized | User is not authenticated | Request without login                      |
| 403 Forbidden    | User has no permission    | Production user requests report            |
| 404 Not Found    | Resource does not exist   | Invalid project ID                         |
| 409 Conflict     | Business rule conflict    | Overlapping timer or active project report |

---

# 14. API Testing Risks

| Risk                                                   | Impact                    | Priority |
| ------------------------------------------------------ | ------------------------- | -------- |
| API returns data from another team                     | Data privacy issue        | High     |
| API allows overlapping timers                          | Incorrect time reports    | High     |
| API allows report for active project                   | Incomplete report data    | High     |
| API accepts expired QR token                           | Unauthorized access       | High     |
| API allows production user to access manager endpoints | Role-based access failure | High     |

---

# 15. Notes

API testing should verify not only positive scenarios but also negative and security-related cases.

Special attention should be paid to:

* correct HTTP status codes
* validation of required fields
* role-based access restrictions
* team data separation
* QR token expiration
* prevention of overlapping time entries
* report generation only after project completion
