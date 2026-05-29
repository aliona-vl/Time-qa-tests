# Test Cases: Project Creation

## Project: Project-Based Time Tracking Web Application

## Test Object

Project creation functionality in the manager dashboard.

## Test Basis

* Manager can create a new project.
* Project must be assigned to the correct team.
* Required fields must be validated.
* Created project must appear on the manager dashboard.
* Project must have an initial status after creation.
* Users without manager permissions must not create team projects.

---

## Test Conditions

| ID            | Test Condition                        | Priority |
| ------------- | ------------------------------------- | -------- |
| TCND-PROJ-001 | Create project with valid data        | High     |
| TCND-PROJ-002 | Validate required project fields      | High     |
| TCND-PROJ-003 | Display created project on dashboard  | High     |
| TCND-PROJ-004 | Assign project to correct team        | High     |
| TCND-PROJ-005 | Set initial project status            | Medium   |
| TCND-PROJ-006 | Prevent unauthorized project creation | High     |

---

## Test Data

| Data Type       | Example                                           |
| --------------- | ------------------------------------------------- |
| Manager user    | [manager@test.com](mailto:manager@test.com)       |
| Production user | [production@test.com](mailto:production@test.com) |
| Project name    | Test Project A                                    |
| Customer        | Test Customer GmbH                                |
| Activity        | Drawing, Meeting, Production, Installation        |
| Employee        | Max Tester                                        |
| Project status  | Active                                            |
| Team code       | TEAM-TEST-001                                     |

---

## Test Cases

| Test Case ID | Test Condition                               | Preconditions                         | Test Steps                                                                                                                                                                     | Test Data                                         | Expected Result                                                                    | Priority | Status  |
| ------------ | -------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- | ---------------------------------------------------------------------------------- | -------- | ------- |
| PROJ-001     | Create project with valid data               | Manager is logged in                  | 1. Open manager dashboard. <br> 2. Click “Create project”. <br> 3. Enter valid project name. <br> 4. Select customer. <br> 5. Add required project data. <br> 6. Save project. | Test Project A                                    | Project is created successfully.                                                   | High     | Not Run |
| PROJ-002     | Created project appears on dashboard         | Project was created successfully      | 1. Return to manager dashboard. <br> 2. Check project list or project tiles.                                                                                                   | Test Project A                                    | Created project is visible on the dashboard.                                       | High     | Not Run |
| PROJ-003     | Project has correct initial status           | Project was created successfully      | 1. Open dashboard. <br> 2. Check project status.                                                                                                                               | New project                                       | Project has initial status, for example “Active”.                                  | Medium   | Not Run |
| PROJ-004     | Create project without project name          | Manager is logged in                  | 1. Open project creation form. <br> 2. Leave project name empty. <br> 3. Fill other fields. <br> 4. Save project.                                                              | Empty project name                                | Project is not created. Validation message is displayed.                           | High     | Not Run |
| PROJ-005     | Create project without required customer     | Manager is logged in                  | 1. Open project creation form. <br> 2. Enter project name. <br> 3. Leave customer empty. <br> 4. Save project.                                                                 | Empty customer                                    | Project is not created or validation message is displayed if customer is required. | High     | Not Run |
| PROJ-006     | Create project with duplicate project name   | Project with same name already exists | 1. Open project creation form. <br> 2. Enter existing project name. <br> 3. Save project.                                                                                      | Test Project A                                    | System prevents duplicate project or clearly separates projects by ID/date/team.   | Medium   | Not Run |
| PROJ-007     | Project is assigned to correct team          | Manager belongs to a team             | 1. Create a new project. <br> 2. Log in as user from same team. <br> 3. Open dashboard.                                                                                        | TEAM-TEST-001                                     | Project is visible only for users of the same team according to role permissions.  | High     | Not Run |
| PROJ-008     | Project is not visible for another team      | Two teams exist                       | 1. Create project as manager of Team A. <br> 2. Log in as manager of Team B. <br> 3. Open dashboard.                                                                           | Team A / Team B                                   | Project from Team A is not visible for Team B.                                     | High     | Not Run |
| PROJ-009     | Production user cannot create team project   | Production user is logged in          | 1. Log in as production user. <br> 2. Try to open project creation page directly.                                                                                              | [production@test.com](mailto:production@test.com) | Access is denied or project creation option is not available.                      | High     | Not Run |
| PROJ-010     | Project details can be opened after creation | Project was created successfully      | 1. Open dashboard. <br> 2. Click created project.                                                                                                                              | Test Project A                                    | Project detail page opens successfully.                                            | High     | Not Run |
| PROJ-011     | Project can contain activities               | Manager is logged in, project exists  | 1. Open project. <br> 2. Add or select activity.                                                                                                                               | Drawing / Production                              | Activity is available for time tracking.                                           | High     | Not Run |
| PROJ-012     | Project can contain employees                | Manager is logged in, project exists  | 1. Open project. <br> 2. Add or select employee.                                                                                                                               | Max Tester                                        | Employee is available for project-related time tracking.                           | High     | Not Run |

---

## Negative Test Cases

| Test Case ID | Scenario                                               | Expected Result                                                          |
| ------------ | ------------------------------------------------------ | ------------------------------------------------------------------------ |
| NEG-PROJ-001 | Project name is empty                                  | Project is not created. Validation message is displayed.                 |
| NEG-PROJ-002 | Required customer is missing                           | Project is not created or validation message is displayed.               |
| NEG-PROJ-003 | Production user opens project creation page            | Access is denied.                                                        |
| NEG-PROJ-004 | User from another team tries to access created project | Access is denied.                                                        |
| NEG-PROJ-005 | Duplicate project name is entered                      | System handles duplicate safely and does not overwrite existing project. |

---

## Traceability Matrix

| Requirement ID | Related Acceptance Criteria | Test Case ID       |
| -------------- | --------------------------- | ------------------ |
| REQ-PROJ-001   | AC-PROJ-001                 | PROJ-001           |
| REQ-PROJ-002   | AC-PROJ-002                 | PROJ-004           |
| REQ-PROJ-003   | AC-PROJ-003                 | PROJ-007, PROJ-008 |
| REQ-PROJ-004   | AC-PROJ-004                 | PROJ-002           |
| REQ-PROJ-005   | AC-PROJ-005                 | PROJ-003           |
| REQ-PROJ-006   | AC-PROJ-006                 | PROJ-004, PROJ-005 |
| REQ-ROLE-001   | AC-ROLE-005                 | PROJ-009           |

---

## Notes

Project creation is a critical workflow because all time entries, activities, employees and reports depend on a correctly created project.

Special attention should be paid to:

* validation of required fields
* correct team assignment
* visibility of created projects
* protection against unauthorized project creation
* correct initial project status
* connection between project, activities and employees
