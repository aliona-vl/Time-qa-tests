# Test Cases: Manager Dashboard

## Project: Project-Based Time Tracking Web Application

## Test Object

Manager dashboard functionality.

## Test Basis

* Manager can access the dashboard after successful login.
* Dashboard displays projects as tiles or cards.
* Manager can create new projects.
* Manager can open existing projects.
* Project status is visible.
* Manager can generate QR access for production users or installers.
* Non-manager users must not access manager-only dashboard functions.

---

## Test Conditions

| ID            | Test Condition                                    | Priority |
| ------------- | ------------------------------------------------- | -------- |
| TCND-DASH-001 | Manager dashboard is displayed after login        | High     |
| TCND-DASH-002 | Project tiles are displayed correctly             | High     |
| TCND-DASH-003 | Project status is visible                         | High     |
| TCND-DASH-004 | Manager can open project details                  | High     |
| TCND-DASH-005 | Manager can create a new project                  | High     |
| TCND-DASH-006 | Manager can access QR generation                  | High     |
| TCND-DASH-007 | Non-manager users cannot access manager dashboard | High     |

---

## Test Data

| Data Type        | Example                                           |
| ---------------- | ------------------------------------------------- |
| Manager user     | [manager@test.com](mailto:manager@test.com)       |
| Production user  | [production@test.com](mailto:production@test.com) |
| Installer access | QR link                                           |
| Existing project | Test Project A                                    |
| Project status   | Active, Paused, Completed                         |
| Browser          | Google Chrome                                     |

---

## Test Cases

| Test Case ID | Test Condition                                     | Preconditions                              | Test Steps                                                                        | Test Data                                         | Expected Result                                                      | Priority | Status  |
| ------------ | -------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------- | -------- | ------- |
| DASH-001     | Manager dashboard is displayed after login         | Manager user exists                        | 1. Open login page. <br> 2. Log in as manager.                                    | [manager@test.com](mailto:manager@test.com)       | Manager dashboard is displayed successfully.                         | High     | Not Run |
| DASH-002     | Project tiles are visible                          | Manager is logged in and projects exist    | 1. Open manager dashboard. <br> 2. Check project area.                            | Existing projects                                 | Project tiles or cards are displayed.                                | High     | Not Run |
| DASH-003     | Empty dashboard state is displayed                 | Manager is logged in and no projects exist | 1. Open manager dashboard.                                                        | No projects                                       | Empty state or message is displayed clearly.                         | Medium   | Not Run |
| DASH-004     | Project status is visible                          | At least one project exists                | 1. Open manager dashboard. <br> 2. Check project tile.                            | Active project                                    | Project status is visible on the project tile.                       | High     | Not Run |
| DASH-005     | Open project from dashboard                        | Manager is logged in and project exists    | 1. Open dashboard. <br> 2. Click on project tile.                                 | Test Project A                                    | Project details page is opened.                                      | High     | Not Run |
| DASH-006     | Create new project from dashboard                  | Manager is logged in                       | 1. Open dashboard. <br> 2. Click “Create project” or similar button.              | New project button                                | Project creation page or form is opened.                             | High     | Not Run |
| DASH-007     | Refresh dashboard after project creation           | New project was created                    | 1. Create a new project. <br> 2. Return to dashboard.                             | New project                                       | New project appears on the dashboard.                                | High     | Not Run |
| DASH-008     | Generate QR access from dashboard or project area  | Manager is logged in and project exists    | 1. Open project. <br> 2. Click QR access option.                                  | Project with QR function                          | QR code or QR link is generated successfully.                        | High     | Not Run |
| DASH-009     | Production user tries to open manager dashboard    | Production user exists                     | 1. Log in as production user. <br> 2. Try to open manager dashboard URL directly. | [production@test.com](mailto:production@test.com) | Access is denied or user is redirected.                              | High     | Not Run |
| DASH-010     | Installer tries to open manager dashboard          | Installer has QR access only               | 1. Open installer QR page. <br> 2. Try to access manager dashboard URL.           | Installer QR link                                 | Access is denied.                                                    | High     | Not Run |
| DASH-011     | Personal user sees only personal projects          | User registered without team code exists   | 1. Log in as personal user. <br> 2. Open dashboard.                               | Personal user                                     | Only personal projects are displayed. Team projects are not visible. | High     | Not Run |
| DASH-012     | Dashboard does not show projects from another team | Two teams exist                            | 1. Log in as manager of Team A. <br> 2. Open dashboard.                           | Team A / Team B                                   | Only projects from Team A are displayed.                             | High     | Not Run |

---

## Negative Test Cases

| Test Case ID | Scenario                                             | Expected Result                                       |
| ------------ | ---------------------------------------------------- | ----------------------------------------------------- |
| NEG-DASH-001 | Production user opens manager dashboard URL directly | Access is denied.                                     |
| NEG-DASH-002 | Installer opens manager dashboard URL directly       | Access is denied.                                     |
| NEG-DASH-003 | Personal user tries to access team project           | Access is denied.                                     |
| NEG-DASH-004 | Manager opens dashboard when no projects exist       | Empty state is displayed, application does not crash. |
| NEG-DASH-005 | User from Team A tries to see Team B projects        | Projects from another team are not visible.           |

---

## Traceability Matrix

| Requirement ID | Related Acceptance Criteria | Test Case ID                           |
| -------------- | --------------------------- | -------------------------------------- |
| REQ-DASH-001   | AC-DASH-001                 | DASH-001, DASH-002                     |
| REQ-DASH-002   | AC-DASH-002                 | DASH-002                               |
| REQ-DASH-003   | AC-DASH-003                 | DASH-004                               |
| REQ-DASH-004   | AC-DASH-004                 | DASH-005                               |
| REQ-DASH-005   | AC-DASH-005                 | DASH-006, DASH-007                     |
| REQ-DASH-006   | AC-DASH-006                 | DASH-009, DASH-010                     |
| REQ-ROLE-001   | AC-ROLE-001, AC-ROLE-005    | DASH-009, DASH-010, DASH-011, DASH-012 |

---

## Notes

The manager dashboard is a business-critical area because it is the central entry point for project management and time tracking.

Special attention should be paid to:

* correct project visibility
* correct project status display
* dashboard access only for authorized users
* separation between team projects and personal projects
* visibility of newly created projects
* access to QR generation only for manager role
