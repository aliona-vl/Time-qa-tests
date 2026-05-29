# Role-Based Access Checklist

## Project: Project-Based Time Tracking Web Application

## Purpose

This checklist is used to verify that each user role has access only to the functions and data allowed for that role.

Role-based access testing is critical because the application contains different user areas for manager, production users, installers and personal users without team code.

---

## Test Object

Role-based access control for the project-based time tracking web application.

---

## Roles Covered

| Role              | Description                                                                      |
| ----------------- | -------------------------------------------------------------------------------- |
| Manager           | Full access to project management, QR generation, project completion and reports |
| Production user   | Limited access to production-related projects and time tracking                  |
| Installer         | Temporary QR-based access to a minimalistic time tracking page                   |
| Personal user     | User registered without team code, can work only with personal projects          |
| Unauthorized user | User without login or invalid access                                             |

---

## Manager Access Checklist

| ID           | Check                                                 | Expected Result                                                  | Priority | Status  |
| ------------ | ----------------------------------------------------- | ---------------------------------------------------------------- | -------- | ------- |
| RBAC-MAN-001 | Manager can log in successfully                       | Manager is redirected to manager dashboard.                      | High     | Not Run |
| RBAC-MAN-002 | Manager can see manager dashboard                     | Dashboard is displayed with project overview.                    | High     | Not Run |
| RBAC-MAN-003 | Manager can create new projects                       | Project creation function is available.                          | High     | Not Run |
| RBAC-MAN-004 | Manager can open project details                      | Project detail page opens successfully.                          | High     | Not Run |
| RBAC-MAN-005 | Manager can start and stop time tracking              | Time tracking works for selected project, activity and employee. | High     | Not Run |
| RBAC-MAN-006 | Manager can create manual time entries                | Manual time entry function is available.                         | Medium   | Not Run |
| RBAC-MAN-007 | Manager can generate QR codes                         | QR generation function is available.                             | High     | Not Run |
| RBAC-MAN-008 | Manager can complete projects                         | Project completion function is available.                        | High     | Not Run |
| RBAC-MAN-009 | Manager can generate reports after project completion | Report generation works for completed projects.                  | High     | Not Run |
| RBAC-MAN-010 | Manager can analyze time by employee and activity     | Report shows grouped time data.                                  | High     | Not Run |

---

## Production User Access Checklist

| ID            | Check                                                         | Expected Result                               | Priority | Status  |
| ------------- | ------------------------------------------------------------- | --------------------------------------------- | -------- | ------- |
| RBAC-PROD-001 | Production user can access production dashboard               | Production dashboard is displayed.            | High     | Not Run |
| RBAC-PROD-002 | Production user sees only production-related projects         | Only allowed production projects are visible. | High     | Not Run |
| RBAC-PROD-003 | Production user can open assigned project                     | Project opens successfully.                   | High     | Not Run |
| RBAC-PROD-004 | Production user can start time tracking                       | Timer starts for allowed production task.     | High     | Not Run |
| RBAC-PROD-005 | Production user can stop time tracking                        | Timer stops and entry is saved.               | High     | Not Run |
| RBAC-PROD-006 | Production user cannot create manager projects                | Project creation as manager is not available. | High     | Not Run |
| RBAC-PROD-007 | Production user cannot access manager reports                 | Report page is blocked.                       | High     | Not Run |
| RBAC-PROD-008 | Production user cannot generate QR codes                      | QR generation is not available.               | High     | Not Run |
| RBAC-PROD-009 | Production user cannot complete project as manager            | Project completion function is blocked.       | High     | Not Run |
| RBAC-PROD-010 | Production user cannot access manager dashboard by direct URL | Access is denied or user is redirected.       | High     | Not Run |

---

## Installer QR Access Checklist

| ID           | Check                                        | Expected Result                             | Priority | Status  |
| ------------ | -------------------------------------------- | ------------------------------------------- | -------- | ------- |
| RBAC-INS-001 | Installer can open valid QR link             | Minimalistic installer page is displayed.   | High     | Not Run |
| RBAC-INS-002 | Installer can see only assigned project/task | No unrelated projects are visible.          | High     | Not Run |
| RBAC-INS-003 | Installer can start time tracking            | Timer starts successfully.                  | High     | Not Run |
| RBAC-INS-004 | Installer can stop time tracking             | Timer stops and time entry is saved.        | High     | Not Run |
| RBAC-INS-005 | Installer cannot access manager dashboard    | Access is denied.                           | High     | Not Run |
| RBAC-INS-006 | Installer cannot access report page          | Access is denied.                           | High     | Not Run |
| RBAC-INS-007 | Installer cannot generate QR codes           | QR generation function is not available.    | High     | Not Run |
| RBAC-INS-008 | Installer cannot create projects             | Project creation function is not available. | High     | Not Run |
| RBAC-INS-009 | Expired installer QR code is rejected        | Access is denied after expiration.          | High     | Not Run |
| RBAC-INS-010 | Invalid installer QR code is rejected        | Access is denied.                           | High     | Not Run |

---

## Personal User Access Checklist

| ID            | Check                                          | Expected Result                           | Priority | Status  |
| ------------- | ---------------------------------------------- | ----------------------------------------- | -------- | ------- |
| RBAC-PERS-001 | User without team code can log in              | User is redirected to personal workspace. | High     | Not Run |
| RBAC-PERS-002 | Personal user can create personal projects     | Personal project creation works.          | High     | Not Run |
| RBAC-PERS-003 | Personal user sees only own projects           | No team projects are visible.             | High     | Not Run |
| RBAC-PERS-004 | Personal user cannot access team dashboard     | Access is denied.                         | High     | Not Run |
| RBAC-PERS-005 | Personal user cannot open team project by URL  | Access is denied.                         | High     | Not Run |
| RBAC-PERS-006 | Personal user data is separated from team data | Only personal data is displayed.          | High     | Not Run |

---

## Unauthorized Access Checklist

| ID              | Check                                | Expected Result                                       | Priority | Status  |
| --------------- | ------------------------------------ | ----------------------------------------------------- | -------- | ------- |
| RBAC-UNAUTH-001 | User opens dashboard without login   | User is redirected to login page or access is denied. | High     | Not Run |
| RBAC-UNAUTH-002 | User opens project URL without login | Access is denied.                                     | High     | Not Run |
| RBAC-UNAUTH-003 | User opens report URL without login  | Access is denied.                                     | High     | Not Run |
| RBAC-UNAUTH-004 | User opens QR URL with invalid token | Access is denied.                                     | High     | Not Run |
| RBAC-UNAUTH-005 | User modifies project ID in URL      | Access to unauthorized project is denied.             | High     | Not Run |
| RBAC-UNAUTH-006 | User modifies team ID in URL         | Access to another team’s data is denied.              | High     | Not Run |

---

## Team Data Separation Checklist

| ID            | Check                                         | Expected Result                  | Priority | Status  |
| ------------- | --------------------------------------------- | -------------------------------- | -------- | ------- |
| RBAC-TEAM-001 | Team A manager sees only Team A projects      | Team B projects are not visible. | High     | Not Run |
| RBAC-TEAM-002 | Team B manager sees only Team B projects      | Team A projects are not visible. | High     | Not Run |
| RBAC-TEAM-003 | Team A user cannot open Team B project by URL | Access is denied.                | High     | Not Run |
| RBAC-TEAM-004 | Team A report does not include Team B data    | Only Team A data is shown.       | High     | Not Run |
| RBAC-TEAM-005 | Team A QR code cannot access Team B project   | Access is denied.                | High     | Not Run |

---

## Access Control Risks

| Risk                                           | Impact                                   | Priority |
| ---------------------------------------------- | ---------------------------------------- | -------- |
| Production user can access manager dashboard   | Unauthorized access to management data   | High     |
| Installer can open report page                 | Confidential project data may be exposed | High     |
| Personal user can access team project          | Team data separation is broken           | High     |
| User can modify URL and access another project | Unauthorized project access              | High     |
| Expired QR code still works                    | Uncontrolled long-term access            | High     |
| Report includes data from another team         | Incorrect and unsafe reporting           | High     |

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

Role-based access testing should be performed after every change related to:

* login
* registration
* team code logic
* dashboard access
* QR access
* project permissions
* report permissions
* URL routing

Any failure in role-based access should be treated as high priority because it can lead to unauthorized data access or incorrect business workflows.
