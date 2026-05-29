# Test Cases: Role-Based Access

## Project: Project-Based Time Tracking Web Application

## Test Object

Role-based access control for manager, production user, installer and personal user.

## Test Basis

* The application provides different access levels for different user roles.
* Manager has access to project management, QR generation, project completion and reports.
* Production user has access only to production-related time tracking.
* Installer has limited QR-based access.
* User without team code can manage only personal projects.
* Users must not access unauthorized pages, data or functions.

---

## Test Conditions

| ID            | Test Condition                                | Priority |
| ------------- | --------------------------------------------- | -------- |
| TCND-ROLE-001 | Manager has access to manager dashboard       | High     |
| TCND-ROLE-002 | Production user has limited production access | High     |
| TCND-ROLE-003 | Installer has only QR-based access            | High     |
| TCND-ROLE-004 | Personal user sees only personal projects     | High     |
| TCND-ROLE-005 | Unauthorized access is blocked                | High     |
| TCND-ROLE-006 | Users cannot access data from other teams     | High     |

---

## Test Data

| Data Type        | Example                                           |
| ---------------- | ------------------------------------------------- |
| Manager user     | [manager@test.com](mailto:manager@test.com)       |
| Production user  | [production@test.com](mailto:production@test.com) |
| Installer access | valid QR link                                     |
| Personal user    | [personal@test.com](mailto:personal@test.com)     |
| Team A           | TEAM-A                                            |
| Team B           | TEAM-B                                            |
| Project A        | Team A Project                                    |
| Project B        | Team B Project                                    |

---

## Test Cases

| Test Case ID | Test Condition                                     | Preconditions                                  | Test Steps                                                                          | Test Data                                         | Expected Result                             | Priority | Status  |
| ------------ | -------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------- | -------- | ------- |
| ROLE-001     | Manager accesses manager dashboard                 | Manager user exists                            | 1. Log in as manager. <br> 2. Open manager dashboard.                               | [manager@test.com](mailto:manager@test.com)       | Manager dashboard is displayed.             | High     | Not Run |
| ROLE-002     | Manager can create project                         | Manager is logged in                           | 1. Open manager dashboard. <br> 2. Click create project.                            | Manager role                                      | Project creation function is available.     | High     | Not Run |
| ROLE-003     | Manager can generate QR access                     | Manager is logged in and project exists        | 1. Open project. <br> 2. Open QR access function. <br> 3. Generate QR code or link. | Existing project                                  | QR access is generated successfully.        | High     | Not Run |
| ROLE-004     | Manager can complete project                       | Manager is logged in and active project exists | 1. Open active project. <br> 2. Click complete project.                             | Active project                                    | Project status changes to completed.        | High     | Not Run |
| ROLE-005     | Manager can generate report                        | Manager is logged in and project is completed  | 1. Open completed project. <br> 2. Generate report.                                 | Completed project                                 | Report is generated successfully.           | High     | Not Run |
| ROLE-006     | Production user opens production dashboard         | Production user exists                         | 1. Log in as production user. <br> 2. Open dashboard.                               | [production@test.com](mailto:production@test.com) | Production dashboard is displayed.          | High     | Not Run |
| ROLE-007     | Production user sees only production tasks         | Production user is logged in                   | 1. Open production dashboard. <br> 2. Check visible tasks.                          | Production role                                   | Only production-related tasks are visible.  | High     | Not Run |
| ROLE-008     | Production user starts time tracking               | Production user is logged in and task exists   | 1. Select available task. <br> 2. Click Start.                                      | Production task                                   | Time tracking starts successfully.          | High     | Not Run |
| ROLE-009     | Production user cannot access manager dashboard    | Production user is logged in                   | 1. Try to open manager dashboard URL directly.                                      | [production@test.com](mailto:production@test.com) | Access is denied or user is redirected.     | High     | Not Run |
| ROLE-010     | Production user cannot generate reports            | Production user is logged in                   | 1. Try to open report page directly.                                                | [production@test.com](mailto:production@test.com) | Access is denied.                           | High     | Not Run |
| ROLE-011     | Installer opens valid QR link                      | Valid QR link exists                           | 1. Open QR link in browser.                                                         | Valid QR link                                     | Minimalistic installer page is displayed.   | High     | Not Run |
| ROLE-012     | Installer can track time via QR page               | Installer page is open                         | 1. Select or confirm task. <br> 2. Start time tracking. <br> 3. Stop time tracking. | Installer task                                    | Installer time entry is saved successfully. | High     | Not Run |
| ROLE-013     | Installer cannot access manager dashboard          | Installer has only QR access                   | 1. Open valid QR page. <br> 2. Try to open manager dashboard URL.                   | Installer QR access                               | Access is denied.                           | High     | Not Run |
| ROLE-014     | Installer cannot generate report                   | Installer has only QR access                   | 1. Try to open report URL directly.                                                 | Installer QR access                               | Access is denied.                           | High     | Not Run |
| ROLE-015     | Personal user sees only personal projects          | User registered without team code exists       | 1. Log in as personal user. <br> 2. Open dashboard.                                 | [personal@test.com](mailto:personal@test.com)     | Only personal projects are visible.         | High     | Not Run |
| ROLE-016     | Personal user cannot access team projects          | Personal user is logged in                     | 1. Try to open team project URL directly.                                           | Team project URL                                  | Access is denied.                           | High     | Not Run |
| ROLE-017     | User from Team A cannot see Team B projects        | Two teams exist                                | 1. Log in as Team A user. <br> 2. Open dashboard.                                   | Team A / Team B                                   | Only Team A projects are visible.           | High     | Not Run |
| ROLE-018     | User from Team A cannot open Team B project by URL | Two teams exist and project URLs are known     | 1. Log in as Team A user. <br> 2. Open Team B project URL directly.                 | Team B project URL                                | Access is denied.                           | High     | Not Run |

---

## Negative Test Cases

| Test Case ID | Scenario                                    | Expected Result   |
| ------------ | ------------------------------------------- | ----------------- |
| NEG-ROLE-001 | Production user opens manager dashboard URL | Access is denied. |
| NEG-ROLE-002 | Production user opens report page           | Access is denied. |
| NEG-ROLE-003 | Installer opens manager dashboard URL       | Access is denied. |
| NEG-ROLE-004 | Installer opens report URL                  | Access is denied. |
| NEG-ROLE-005 | Personal user opens team project URL        | Access is denied. |
| NEG-ROLE-006 | User from Team A opens Team B project URL   | Access is denied. |

---

## Traceability Matrix

| Requirement ID | Related Acceptance Criteria | Test Case ID                                               |
| -------------- | --------------------------- | ---------------------------------------------------------- |
| REQ-ROLE-001   | AC-ROLE-001                 | ROLE-001, ROLE-002, ROLE-003, ROLE-004, ROLE-005           |
| REQ-ROLE-002   | AC-ROLE-002                 | ROLE-006, ROLE-007, ROLE-008, ROLE-009, ROLE-010           |
| REQ-ROLE-003   | AC-ROLE-003                 | ROLE-011, ROLE-012, ROLE-013, ROLE-014                     |
| REQ-ROLE-004   | AC-ROLE-004                 | ROLE-015, ROLE-016                                         |
| REQ-ROLE-005   | AC-ROLE-005                 | ROLE-009, ROLE-010, ROLE-013, ROLE-014, ROLE-016, ROLE-018 |
| REQ-ROLE-006   | AC-ROLE-006                 | ROLE-017, ROLE-018                                         |

---

## Notes

Role-based access is one of the most important security and business logic areas of the application.

Special attention should be paid to:

* correct dashboard per role
* separation between manager, production and installer functions
* direct URL access attempts
* team data separation
* limited QR-based installer access
* protection of reports and project management functions
