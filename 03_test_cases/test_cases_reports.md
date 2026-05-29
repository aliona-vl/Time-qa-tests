# Test Cases: Report Generation and Time Analysis

## Project: Project-Based Time Tracking Web Application

## Test Object

Report generation and analysis of recorded working time after project completion.

## Test Basis

* Manager can complete a project.
* Final report can be generated only after project completion.
* Active projects should not allow final report generation.
* Report must include saved time entries.
* Report must show total project time.
* Report must show working time by employee.
* Report must show working time by activity.
* Report must include production and installer time.
* Report data must match saved time tracking entries.

---

## Test Conditions

| ID           | Test Condition                                  | Priority |
| ------------ | ----------------------------------------------- | -------- |
| TCND-REP-001 | Generate report after project completion        | High     |
| TCND-REP-002 | Prevent report generation before completion     | High     |
| TCND-REP-003 | Display total project time                      | High     |
| TCND-REP-004 | Display time by employee                        | High     |
| TCND-REP-005 | Display time by activity                        | High     |
| TCND-REP-006 | Include production time                         | High     |
| TCND-REP-007 | Include installer time                          | High     |
| TCND-REP-008 | Validate report data against saved time entries | High     |

---

## Test Data

| Data Type         | Example                                     |
| ----------------- | ------------------------------------------- |
| Manager user      | [manager@test.com](mailto:manager@test.com) |
| Active project    | Test Project Active                         |
| Completed project | Test Project Completed                      |
| Employee 1        | Max Tester                                  |
| Employee 2        | Anna Test                                   |
| Activity 1        | Meeting                                     |
| Activity 2        | Production                                  |
| Activity 3        | Installation                                |
| Time entry 1      | Max Tester / Meeting / 60 min               |
| Time entry 2      | Anna Test / Production / 120 min            |
| Time entry 3      | Installer / Installation / 90 min           |

---

## Test Cases

| Test Case ID | Test Condition                                           | Preconditions                                                   | Test Steps                                                                                           | Test Data                                         | Expected Result                                                     | Priority | Status  |
| ------------ | -------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------- | -------- | ------- |
| REP-001      | Generate report after project completion                 | Manager is logged in, project is completed and has time entries | 1. Open completed project. <br> 2. Open report section. <br> 3. Click Generate Report.               | Completed project                                 | Report is generated successfully.                                   | High     | Not Run |
| REP-002      | Prevent report generation before project completion      | Manager is logged in and project is active                      | 1. Open active project. <br> 2. Try to generate final report.                                        | Active project                                    | Report generation is blocked or report button is not available.     | High     | Not Run |
| REP-003      | Report shows total project time                          | Completed project has several time entries                      | 1. Generate report. <br> 2. Check total time value.                                                  | 60 + 120 + 90 min                                 | Total project time is calculated correctly.                         | High     | Not Run |
| REP-004      | Report shows time by employee                            | Completed project has entries for different employees           | 1. Generate report. <br> 2. Check employee section.                                                  | Max Tester, Anna Test                             | Working time is grouped correctly by employee.                      | High     | Not Run |
| REP-005      | Report shows time by activity                            | Completed project has entries for different activities          | 1. Generate report. <br> 2. Check activity section.                                                  | Meeting, Production, Installation                 | Working time is grouped correctly by activity.                      | High     | Not Run |
| REP-006      | Report includes production time                          | Production user has saved time entry                            | 1. Add production time entry. <br> 2. Complete project. <br> 3. Generate report.                     | Production / 120 min                              | Production time is included in the report.                          | High     | Not Run |
| REP-007      | Report includes installer time                           | Installer has saved time entry via QR access                    | 1. Add installer time entry via QR page. <br> 2. Complete project. <br> 3. Generate report.          | Installation / 90 min                             | Installer time is included in the report.                           | High     | Not Run |
| REP-008      | Report data matches saved time entries                   | Project has saved time entries                                  | 1. Open saved time entries. <br> 2. Generate report. <br> 3. Compare report data with saved entries. | Saved time entries                                | Report values match saved time entries.                             | High     | Not Run |
| REP-009      | Report for project without time entries                  | Completed project has no time entries                           | 1. Complete project without time entries. <br> 2. Generate report.                                   | Empty project                                     | Report shows zero time or clear message that no time entries exist. | Medium   | Not Run |
| REP-010      | Report cannot include data from another project          | Two completed projects exist                                    | 1. Generate report for Project A. <br> 2. Check if Project B entries appear.                         | Project A / Project B                             | Only Project A data is included.                                    | High     | Not Run |
| REP-011      | Report cannot include data from another team             | Two teams exist with completed projects                         | 1. Log in as Team A manager. <br> 2. Generate report for Team A project.                             | Team A / Team B                                   | Report includes only Team A project data.                           | High     | Not Run |
| REP-012      | Completed project status remains after report generation | Project is completed                                            | 1. Generate report. <br> 2. Return to project overview. <br> 3. Check project status.                | Completed project                                 | Project status remains completed.                                   | Medium   | Not Run |
| REP-013      | Report page is not accessible for production user        | Production user exists                                          | 1. Log in as production user. <br> 2. Try to open report page directly.                              | [production@test.com](mailto:production@test.com) | Access is denied.                                                   | High     | Not Run |
| REP-014      | Report page is not accessible for installer              | Installer has QR access only                                    | 1. Open QR page. <br> 2. Try to open report URL directly.                                            | Installer QR access                               | Access is denied.                                                   | High     | Not Run |
| REP-015      | Manual time entries are included in report               | Project has manual time entry                                   | 1. Add manual time entry. <br> 2. Complete project. <br> 3. Generate report.                         | Manual entry                                      | Manual time entry is included in the report.                        | High     | Not Run |

---

## Negative Test Cases

| Test Case ID | Scenario                                            | Expected Result                                            |
| ------------ | --------------------------------------------------- | ---------------------------------------------------------- |
| NEG-REP-001  | Manager tries to generate report for active project | Report generation is blocked.                              |
| NEG-REP-002  | Production user opens report page                   | Access is denied.                                          |
| NEG-REP-003  | Installer opens report page                         | Access is denied.                                          |
| NEG-REP-004  | Report for Project A includes Project B data        | This must not happen; only selected project data is shown. |
| NEG-REP-005  | Report contains data from another team              | This must not happen; team data must be separated.         |
| NEG-REP-006  | Report is generated with missing required data      | Clear message is displayed or generation is blocked.       |

---

## Traceability Matrix

| Requirement ID | Related Acceptance Criteria | Test Case ID              |
| -------------- | --------------------------- | ------------------------- |
| REQ-COMP-001   | AC-COMP-001                 | REP-001                   |
| REQ-COMP-002   | AC-COMP-002                 | REP-012                   |
| REQ-COMP-003   | AC-COMP-003                 | REP-001                   |
| REQ-COMP-004   | AC-COMP-004                 | REP-002                   |
| REQ-COMP-005   | AC-COMP-005                 | REP-001, REP-008          |
| REQ-REP-001    | AC-REP-001                  | REP-001                   |
| REQ-REP-002    | AC-REP-002                  | REP-003                   |
| REQ-REP-003    | AC-REP-003                  | REP-004                   |
| REQ-REP-004    | AC-REP-004                  | REP-005                   |
| REQ-REP-005    | AC-REP-005                  | REP-006                   |
| REQ-REP-006    | AC-REP-006                  | REP-007                   |
| REQ-REP-007    | AC-REP-007                  | REP-008, REP-010, REP-011 |
| REQ-REP-008    | AC-REP-008                  | REP-009                   |
| REQ-ROLE-001   | AC-ROLE-005                 | REP-013, REP-014          |

---

## Notes

Report generation is business-critical because it provides the final basis for project analysis and management decisions.

Special attention should be paid to:

* report generation only after project completion
* correct total time calculation
* correct grouping by employee
* correct grouping by activity
* inclusion of production and installer time
* exclusion of data from other projects or teams
* access restriction for non-manager users
