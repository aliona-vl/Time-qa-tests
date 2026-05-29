# Acceptance Criteria

## Project: Project-Based Time Tracking Web Application

This document defines acceptance criteria for the main features of the time tracking application.

Acceptance criteria describe the conditions that must be fulfilled for a feature to be considered correctly implemented and ready for testing.

---

## 1. Registration with Team Code

### User Story

As a user, I want to register with a team code so that I can join an existing team and work with shared team projects.

### Acceptance Criteria

| ID         | Acceptance Criterion                                                               | Priority |
| ---------- | ---------------------------------------------------------------------------------- | -------- |
| AC-REG-001 | User can register with valid personal data and a valid team code.                  | High     |
| AC-REG-002 | User with valid team code is assigned to the correct team.                         | High     |
| AC-REG-003 | User can register without team code and receives access only to personal projects. | High     |
| AC-REG-004 | Invalid team code is rejected with a clear error message.                          | High     |
| AC-REG-005 | Required fields cannot be empty during registration.                               | High     |
| AC-REG-006 | User from one team cannot access projects from another team.                       | High     |

---

## 2. Login

### User Story

As a registered user, I want to log in so that I can access the application according to my role.

### Acceptance Criteria

| ID         | Acceptance Criterion                                      | Priority |
| ---------- | --------------------------------------------------------- | -------- |
| AC-LOG-001 | User can log in with valid email and password.            | High     |
| AC-LOG-002 | User cannot log in with incorrect password.               | High     |
| AC-LOG-003 | User cannot log in with unknown email address.            | High     |
| AC-LOG-004 | Empty login fields show validation messages.              | Medium   |
| AC-LOG-005 | After login, user is redirected to the correct dashboard. | High     |
| AC-LOG-006 | User session is created after successful login.           | High     |

---

## 3. Manager Dashboard

### User Story

As a manager, I want to see a dashboard with all relevant projects so that I can manage and control project work.

### Acceptance Criteria

| ID          | Acceptance Criterion                                              | Priority |
| ----------- | ----------------------------------------------------------------- | -------- |
| AC-DASH-001 | Manager can see all team projects.                                | High     |
| AC-DASH-002 | Projects are displayed as clear project cards or tiles.           | Medium   |
| AC-DASH-003 | Project status is visible on the dashboard.                       | High     |
| AC-DASH-004 | Manager can open project details from the dashboard.              | High     |
| AC-DASH-005 | Manager can create new projects.                                  | High     |
| AC-DASH-006 | Non-manager users cannot access manager-only dashboard functions. | High     |

---

## 4. Project Creation

### User Story

As a manager, I want to create a project so that working time can be tracked for this project.

### Acceptance Criteria

| ID          | Acceptance Criterion                                   | Priority |
| ----------- | ------------------------------------------------------ | -------- |
| AC-PROJ-001 | Manager can create a project with valid required data. | High     |
| AC-PROJ-002 | Project name is required.                              | High     |
| AC-PROJ-003 | Project is assigned to the correct team.               | High     |
| AC-PROJ-004 | Created project appears on the manager dashboard.      | High     |
| AC-PROJ-005 | Project has an initial status after creation.          | Medium   |
| AC-PROJ-006 | Empty required fields show validation messages.        | High     |

---

## 5. Start/Stop Time Tracking

### User Story

As a user, I want to start and stop time tracking so that my working time is recorded correctly for a selected project and activity.

### Acceptance Criteria

| ID          | Acceptance Criterion                                                         | Priority |
| ----------- | ---------------------------------------------------------------------------- | -------- |
| AC-TIME-001 | User can start time tracking after selecting project, activity and employee. | High     |
| AC-TIME-002 | User can stop active time tracking.                                          | High     |
| AC-TIME-003 | Start time, stop time and duration are saved correctly.                      | High     |
| AC-TIME-004 | Time entry is assigned to the correct project.                               | High     |
| AC-TIME-005 | Time entry is assigned to the selected activity.                             | High     |
| AC-TIME-006 | Time entry is assigned to the selected employee.                             | High     |
| AC-TIME-007 | System prevents overlapping active time entries for the same user.           | High     |
| AC-TIME-008 | User cannot start tracking without selecting required fields.                | High     |

---

## 6. Manual Time Entry

### User Story

As a manager, I want to add time entries manually so that missing or forgotten working times can be documented later.

### Acceptance Criteria

| ID         | Acceptance Criterion                                                             | Priority |
| ---------- | -------------------------------------------------------------------------------- | -------- |
| AC-MAN-001 | User can create a manual time entry with valid data.                             | Medium   |
| AC-MAN-002 | Manual time entry requires project, activity, employee, start time and end time. | High     |
| AC-MAN-003 | End time cannot be earlier than start time.                                      | High     |
| AC-MAN-004 | Manual time entry is saved in the correct project.                               | High     |
| AC-MAN-005 | Manual entries are included in reports.                                          | High     |

---

## 7. Production Dashboard

### User Story

As a production employee, I want to see only production-related tasks so that I can record my working time without unnecessary management functions.

### Acceptance Criteria

| ID          | Acceptance Criterion                                 | Priority |
| ----------- | ---------------------------------------------------- | -------- |
| AC-PROD-001 | Production user can access production dashboard.     | High     |
| AC-PROD-002 | Production user sees only relevant production tasks. | High     |
| AC-PROD-003 | Production user can start and stop time tracking.    | High     |
| AC-PROD-004 | Production user cannot access manager reports.       | High     |
| AC-PROD-005 | Production user cannot manage all projects.          | High     |

---

## 8. Installer QR Access

### User Story

As an installer, I want to access a simple time tracking page via QR code so that I can record working time without a full user account.

### Acceptance Criteria

| ID        | Acceptance Criterion                                         | Priority |
| --------- | ------------------------------------------------------------ | -------- |
| AC-QR-001 | Manager can generate QR access for installer.                | High     |
| AC-QR-002 | Installer can open the page with a valid QR code.            | High     |
| AC-QR-003 | Installer sees a minimalistic time tracking page.            | Medium   |
| AC-QR-004 | Installer can record working time through the QR page.       | High     |
| AC-QR-005 | Expired QR code is rejected.                                 | High     |
| AC-QR-006 | Invalid QR code is rejected.                                 | High     |
| AC-QR-007 | Installer access is limited to the assigned project or task. | High     |

---

## 9. Project Completion

### User Story

As a manager, I want to complete a project so that the final report can be generated based on complete time data.

### Acceptance Criteria

| ID          | Acceptance Criterion                                                | Priority |
| ----------- | ------------------------------------------------------------------- | -------- |
| AC-COMP-001 | Manager can mark a project as completed.                            | High     |
| AC-COMP-002 | Completed project changes its status.                               | High     |
| AC-COMP-003 | Final report generation is available only after project completion. | High     |
| AC-COMP-004 | Active projects cannot be used for final report generation.         | High     |
| AC-COMP-005 | Completed project data remains available for analysis.              | High     |

---

## 10. Report Generation

### User Story

As a manager, I want to generate a report after project completion so that I can analyze working time by employee and activity.

### Acceptance Criteria

| ID         | Acceptance Criterion                                   | Priority |
| ---------- | ------------------------------------------------------ | -------- |
| AC-REP-001 | Manager can generate report after project completion.  | High     |
| AC-REP-002 | Report shows total project time.                       | High     |
| AC-REP-003 | Report shows time by employee.                         | High     |
| AC-REP-004 | Report shows time by activity.                         | High     |
| AC-REP-005 | Report includes production time.                       | High     |
| AC-REP-006 | Report includes installer time.                        | High     |
| AC-REP-007 | Report data matches saved time entries.                | High     |
| AC-REP-008 | Report is not generated when required data is missing. | Medium   |

---

## 11. Role-Based Access

### User Story

As a system user, I want to access only the features allowed for my role so that project data remains protected and organized.

### Acceptance Criteria

| ID          | Acceptance Criterion                                                 | Priority |
| ----------- | -------------------------------------------------------------------- | -------- |
| AC-ROLE-001 | Manager has access to project management and reports.                | High     |
| AC-ROLE-002 | Production user has access only to production-related time tracking. | High     |
| AC-ROLE-003 | Installer has only QR-based limited access.                          | High     |
| AC-ROLE-004 | Personal user without team code can access only personal projects.   | High     |
| AC-ROLE-005 | Unauthorized access attempts are blocked.                            | High     |
| AC-ROLE-006 | Users cannot see data from other teams.                              | High     |

---

## 12. Acceptance Summary

The application can be accepted for further testing when the following main conditions are fulfilled:

* registration with and without team code works correctly
* login redirects users to the correct dashboard
* manager can create and manage projects
* time tracking can be started and stopped correctly
* manual time entries can be saved
* role-based access is restricted correctly
* QR access works only with valid codes
* final reports are generated only after project completion
* reports show correct time data by employee and activity
