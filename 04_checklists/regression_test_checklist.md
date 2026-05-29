# Regression Test Checklist

## Project: Project-Based Time Tracking Web Application

## Purpose

This regression test checklist is used to verify that existing functionality still works correctly after changes, bug fixes, updates or new feature implementation.

Regression testing is especially important for this application because changes in one module can affect other business-critical workflows such as registration, role-based access, time tracking and report generation.

---

## Test Object

Project-based time tracking web application.

---

## Regression Test Scope

Regression testing covers the following areas:

* registration with and without team code
* login and logout
* manager dashboard
* project creation
* project status handling
* start/stop time tracking
* manual time entry
* production dashboard
* installer QR access
* role-based access
* project completion
* report generation
* data separation between teams and users

---

## Regression Test Checklist

| ID           | Check                                                 | Expected Result                                           | Priority | Status  |
| ------------ | ----------------------------------------------------- | --------------------------------------------------------- | -------- | ------- |
| REG-CHK-001  | Registration with valid team code works               | User is registered and assigned to the correct team.      | High     | Not Run |
| REG-CHK-002  | Registration without team code works                  | User is registered with access only to personal projects. | High     | Not Run |
| REG-CHK-003  | Invalid team code is rejected                         | Error message is displayed and user is not added to team. | High     | Not Run |
| REG-CHK-004  | Required registration fields are validated            | Empty required fields show validation messages.           | High     | Not Run |
| REG-CHK-005  | User from one team cannot see another team’s projects | Data separation works correctly.                          | High     | Not Run |
| LOG-CHK-001  | Login with valid credentials works                    | User is logged in successfully.                           | High     | Not Run |
| LOG-CHK-002  | Login with invalid credentials is rejected            | Error message is displayed.                               | High     | Not Run |
| LOG-CHK-003  | Logout works correctly                                | User session is ended.                                    | High     | Not Run |
| LOG-CHK-004  | Protected pages cannot be accessed without login      | User is redirected or access is denied.                   | High     | Not Run |
| DASH-CHK-001 | Manager dashboard opens correctly                     | Project tiles or project overview are displayed.          | High     | Not Run |
| DASH-CHK-002 | Project status is visible on dashboard                | Correct project status is shown.                          | High     | Not Run |
| DASH-CHK-003 | Created project appears on dashboard                  | New project is visible after creation.                    | High     | Not Run |
| PROJ-CHK-001 | Manager can create project with valid data            | Project is saved successfully.                            | High     | Not Run |
| PROJ-CHK-002 | Project required fields are validated                 | Missing required fields show validation messages.         | High     | Not Run |
| PROJ-CHK-003 | Project is assigned to the correct team               | Only authorized team users can see the project.           | High     | Not Run |
| TIME-CHK-001 | Start time tracking works                             | Timer starts successfully.                                | High     | Not Run |
| TIME-CHK-002 | Stop time tracking works                              | Timer stops and time entry is saved.                      | High     | Not Run |
| TIME-CHK-003 | Duration is calculated correctly                      | Saved duration matches start and stop time.               | High     | Not Run |
| TIME-CHK-004 | Time entry is assigned to correct project             | Entry appears only in selected project.                   | High     | Not Run |
| TIME-CHK-005 | Time entry is assigned to correct activity            | Selected activity is saved correctly.                     | High     | Not Run |
| TIME-CHK-006 | Time entry is assigned to correct employee            | Selected employee is saved correctly.                     | High     | Not Run |
| TIME-CHK-007 | Overlapping time entries are prevented                | Second active timer for same employee is blocked.         | High     | Not Run |
| MAN-CHK-001  | Manual time entry works with valid data               | Manual entry is saved successfully.                       | Medium   | Not Run |
| MAN-CHK-002  | Invalid manual time range is rejected                 | End time before start time is not accepted.               | High     | Not Run |
| ROLE-CHK-001 | Manager has full project access                       | Manager functions are available.                          | High     | Not Run |
| ROLE-CHK-002 | Production user has limited access                    | Only production-related tasks are visible.                | High     | Not Run |
| ROLE-CHK-003 | Installer has only QR-based access                    | Installer cannot access manager functions.                | High     | Not Run |
| ROLE-CHK-004 | Personal user sees only personal projects             | Team projects are not visible.                            | High     | Not Run |
| QR-CHK-001   | Manager can generate installer QR code                | Temporary QR access is generated.                         | High     | Not Run |
| QR-CHK-002   | Valid QR code opens installer page                    | Minimalistic time tracking page is displayed.             | High     | Not Run |
| QR-CHK-003   | Expired QR code is rejected                           | Access is denied after expiration.                        | High     | Not Run |
| QR-CHK-004   | Invalid QR code is rejected                           | Access is denied.                                         | High     | Not Run |
| QR-CHK-005   | Installer time entry is saved correctly               | Entry appears in assigned project.                        | High     | Not Run |
| COMP-CHK-001 | Manager can complete project                          | Project status changes to completed.                      | High     | Not Run |
| COMP-CHK-002 | Report is available only after completion             | Report generation is blocked for active projects.         | High     | Not Run |
| REP-CHK-001  | Report generation works after completion              | Report is generated successfully.                         | High     | Not Run |
| REP-CHK-002  | Report shows total project time                       | Total time is calculated correctly.                       | High     | Not Run |
| REP-CHK-003  | Report shows time by employee                         | Employee-based analysis is correct.                       | High     | Not Run |
| REP-CHK-004  | Report shows time by activity                         | Activity-based analysis is correct.                       | High     | Not Run |
| REP-CHK-005  | Report includes production time                       | Production entries are included.                          | High     | Not Run |
| REP-CHK-006  | Report includes installer time                        | Installer entries are included.                           | High     | Not Run |
| REP-CHK-007  | Report does not include another project’s data        | Only selected project data is shown.                      | High     | Not Run |
| REP-CHK-008  | Report does not include another team’s data           | Team data separation works correctly.                     | High     | Not Run |

---

## Regression Priority Areas

The most important regression areas are:

* team code handling
* login and session handling
* role-based access
* time tracking calculation
* prevention of overlapping time entries
* QR access validation
* project completion logic
* report generation and data accuracy

---

## Status Legend

| Status  | Meaning                                          |
| ------- | ------------------------------------------------ |
| Passed  | Check was executed successfully                  |
| Failed  | Check failed and defect should be reported       |
| Blocked | Check could not be executed due to another issue |
| Not Run | Check has not been executed yet                  |

---

## Regression Testing Notes

Regression testing should be executed after:

* bug fixes
* changes in registration or login
* changes in role permissions
* changes in time tracking logic
* changes in QR access
* changes in report generation
* database structure changes

If a high-priority regression check fails, the defect should be reported and retested after fixing.
