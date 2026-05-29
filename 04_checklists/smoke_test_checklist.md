# Smoke Test Checklist

## Project: Project-Based Time Tracking Web Application

## Purpose

This smoke test checklist is used to verify that the most important functions of the application work after a new build, update or deployment.

Smoke testing helps to quickly decide whether the application is stable enough for deeper functional and regression testing.

---

## Test Object

Project-based time tracking web application.

---

## Smoke Test Scope

The smoke test covers the most critical business functions:

* application availability
* registration
* login
* manager dashboard
* project creation
* start/stop time tracking
* role-based access
* QR access
* project completion
* report generation

---

## Smoke Test Checklist

| ID     | Check                                           | Expected Result                                                 | Priority | Status  |
| ------ | ----------------------------------------------- | --------------------------------------------------------------- | -------- | ------- |
| SM-001 | Application opens successfully                  | Application start page is displayed without server error.       | High     | Not Run |
| SM-002 | Registration page opens                         | Registration form is displayed.                                 | High     | Not Run |
| SM-003 | User can register with valid team code          | User is registered and assigned to the team.                    | High     | Not Run |
| SM-004 | User can register without team code             | User is registered with personal workspace only.                | High     | Not Run |
| SM-005 | Login page opens                                | Login form is displayed.                                        | High     | Not Run |
| SM-006 | Manager can log in                              | Manager is redirected to manager dashboard.                     | High     | Not Run |
| SM-007 | Production user can log in                      | Production user is redirected to production dashboard.          | High     | Not Run |
| SM-008 | Manager dashboard loads correctly               | Project tiles or project overview are displayed.                | High     | Not Run |
| SM-009 | Manager can create a new project                | New project is saved successfully.                              | High     | Not Run |
| SM-010 | Created project appears on dashboard            | Project is visible after creation.                              | High     | Not Run |
| SM-011 | Manager can open project details                | Project detail page opens successfully.                         | High     | Not Run |
| SM-012 | User can start time tracking                    | Timer starts after project, activity and employee are selected. | High     | Not Run |
| SM-013 | User can stop time tracking                     | Timer stops and time entry is saved.                            | High     | Not Run |
| SM-014 | Saved time entry is visible in project          | Time entry appears in the correct project.                      | High     | Not Run |
| SM-015 | Production dashboard opens                      | Production user sees production-related tasks.                  | High     | Not Run |
| SM-016 | Production user cannot access manager dashboard | Access is denied or user is redirected.                         | High     | Not Run |
| SM-017 | Manager can generate QR access                  | QR code or QR link is generated successfully.                   | High     | Not Run |
| SM-018 | Valid installer QR link opens minimal page      | Installer time tracking page is displayed.                      | High     | Not Run |
| SM-019 | Installer can track time through QR page        | Installer time entry is saved successfully.                     | High     | Not Run |
| SM-020 | Manager can complete project                    | Project status changes to completed.                            | High     | Not Run |
| SM-021 | Manager can generate report after completion    | Final report is generated successfully.                         | High     | Not Run |
| SM-022 | Report shows total project time                 | Total time is displayed in the report.                          | High     | Not Run |
| SM-023 | Logout works correctly                          | User is logged out and protected pages are not accessible.      | High     | Not Run |

---

## Pass / Fail Criteria

### Passed

Smoke test is passed when:

* all high-priority checks are passed
* application is stable enough for detailed testing
* no blocker or critical defect is found

### Failed

Smoke test is failed when:

* application cannot be opened
* login does not work
* manager dashboard is not accessible
* project creation does not work
* time tracking cannot be started or stopped
* critical role-based access issue exists
* report generation is not available after project completion

---

## Status Legend

| Status  | Meaning                                          |
| ------- | ------------------------------------------------ |
| Passed  | Check was executed successfully                  |
| Failed  | Check failed and defect should be reported       |
| Blocked | Check could not be executed due to another issue |
| Not Run | Check has not been executed yet                  |

---

## Notes

Smoke testing should be executed before deeper testing activities.

If one of the critical smoke checks fails, further testing should be stopped until the issue is fixed.
