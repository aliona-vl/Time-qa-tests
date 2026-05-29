# Test Cases: Start/Stop Time Tracking

## Project: Project-Based Time Tracking Web Application

## Test Object

Start/Stop time tracking functionality and manual time entry.

## Test Basis

* User can select a project, activity and employee.
* User can start time tracking.
* User can stop active time tracking.
* The system saves start time, stop time and duration.
* Time entry is assigned to the correct project, activity and employee.
* Manual time entry is possible.
* Overlapping time entries should be prevented.

---

## Test Conditions

| ID            | Test Condition                                              | Priority |
| ------------- | ----------------------------------------------------------- | -------- |
| TCND-TIME-001 | Start time tracking with valid data                         | High     |
| TCND-TIME-002 | Stop active time tracking                                   | High     |
| TCND-TIME-003 | Save duration correctly                                     | High     |
| TCND-TIME-004 | Validate required fields                                    | High     |
| TCND-TIME-005 | Prevent overlapping time entries                            | High     |
| TCND-TIME-006 | Add manual time entry                                       | Medium   |
| TCND-TIME-007 | Assign time entry to correct project, activity and employee | High     |

---

## Test Data

| Data Type        | Example                                           |
| ---------------- | ------------------------------------------------- |
| Manager user     | [manager@test.com](mailto:manager@test.com)       |
| Production user  | [production@test.com](mailto:production@test.com) |
| Project          | Test Project A                                    |
| Activity         | Drawing, Meeting, Production, Installation        |
| Employee         | Max Tester                                        |
| Start time       | 08:00                                             |
| End time         | 10:00                                             |
| Invalid end time | 07:30                                             |
| Browser          | Google Chrome                                     |

---

## Test Cases

| Test Case ID | Test Condition                                        | Preconditions                                    | Test Steps                                                                                                                        | Test Data                                                           | Expected Result                                                 | Priority | Status  |
| ------------ | ----------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------- | -------- | ------- |
| TIME-001     | Start time tracking with valid data                   | User is logged in and project exists             | 1. Open project. <br> 2. Select activity. <br> 3. Select employee. <br> 4. Click Start.                                           | Project: Test Project A, Activity: Production, Employee: Max Tester | Timer starts successfully. Start time is recorded.              | High     | Not Run |
| TIME-002     | Stop active time tracking                             | Active timer exists                              | 1. Click Stop.                                                                                                                    | Active timer                                                        | Timer stops successfully. End time and duration are saved.      | High     | Not Run |
| TIME-003     | Save time entry in correct project                    | Active timer was started in selected project     | 1. Start timer in Project A. <br> 2. Stop timer. <br> 3. Open Project A time entries.                                             | Test Project A                                                      | Time entry is visible in the correct project.                   | High     | Not Run |
| TIME-004     | Save selected activity in time entry                  | Activity is selected before start                | 1. Select activity. <br> 2. Start timer. <br> 3. Stop timer. <br> 4. Check saved time entry.                                      | Activity: Production                                                | Saved time entry contains selected activity.                    | High     | Not Run |
| TIME-005     | Save selected employee in time entry                  | Employee is selected before start                | 1. Select employee. <br> 2. Start timer. <br> 3. Stop timer. <br> 4. Check saved time entry.                                      | Employee: Max Tester                                                | Saved time entry contains selected employee.                    | High     | Not Run |
| TIME-006     | Start timer without activity                          | User is logged in and project exists             | 1. Open project. <br> 2. Select employee. <br> 3. Leave activity empty. <br> 4. Click Start.                                      | Empty activity                                                      | Timer does not start. Validation message is displayed.          | High     | Not Run |
| TIME-007     | Start timer without employee                          | User is logged in and project exists             | 1. Open project. <br> 2. Select activity. <br> 3. Leave employee empty. <br> 4. Click Start.                                      | Empty employee                                                      | Timer does not start. Validation message is displayed.          | High     | Not Run |
| TIME-008     | Start timer without project                           | User is logged in                                | 1. Open time tracking page without selected project. <br> 2. Select activity and employee. <br> 3. Click Start.                   | No project selected                                                 | Timer does not start. User must select or open a project first. | High     | Not Run |
| TIME-009     | Prevent overlapping active timer for same employee    | Active timer already exists for employee         | 1. Start timer for employee. <br> 2. Try to start another timer for same employee before stopping first timer.                    | Same employee                                                       | System prevents overlapping active time entry.                  | High     | Not Run |
| TIME-010     | Prevent overlapping active timer in another activity  | Active timer exists for employee in one activity | 1. Start timer for Activity A. <br> 2. Try to start timer for Activity B with same employee.                                      | Same employee, different activity                                   | System prevents second active timer for same employee.          | High     | Not Run |
| TIME-011     | Manual time entry with valid data                     | User is logged in and project exists             | 1. Open project. <br> 2. Select manual time entry. <br> 3. Enter activity, employee, start time and end time. <br> 4. Save entry. | 08:00–10:00                                                         | Manual time entry is saved successfully.                        | Medium   | Not Run |
| TIME-012     | Manual time entry with end time before start time     | User is logged in and project exists             | 1. Open manual time entry. <br> 2. Enter start time 08:00. <br> 3. Enter end time 07:30. <br> 4. Save entry.                      | Start: 08:00, End: 07:30                                            | Entry is rejected. Validation message is displayed.             | High     | Not Run |
| TIME-013     | Manual entry without activity                         | User is logged in and project exists             | 1. Open manual time entry. <br> 2. Leave activity empty. <br> 3. Fill other fields. <br> 4. Save entry.                           | Empty activity                                                      | Manual entry is not saved. Validation message is displayed.     | Medium   | Not Run |
| TIME-014     | Manual entry without employee                         | User is logged in and project exists             | 1. Open manual time entry. <br> 2. Leave employee empty. <br> 3. Fill other fields. <br> 4. Save entry.                           | Empty employee                                                      | Manual entry is not saved. Validation message is displayed.     | Medium   | Not Run |
| TIME-015     | Time entry appears in report after project completion | Project has saved time entry                     | 1. Add time entry. <br> 2. Complete project. <br> 3. Generate report.                                                             | Saved time entry                                                    | Time entry is included in the final report.                     | High     | Not Run |

---

## Negative Test Cases

| Test Case ID | Scenario                                     | Expected Result                                        |
| ------------ | -------------------------------------------- | ------------------------------------------------------ |
| NEG-TIME-001 | Start timer without activity                 | Timer does not start. Validation message is displayed. |
| NEG-TIME-002 | Start timer without employee                 | Timer does not start. Validation message is displayed. |
| NEG-TIME-003 | Start second timer for same employee         | System prevents overlapping time entry.                |
| NEG-TIME-004 | Manual entry with end time before start time | Entry is rejected.                                     |
| NEG-TIME-005 | Manual entry without project                 | Entry is not saved. Project assignment is required.    |

---

## Traceability Matrix

| Requirement ID | Related Acceptance Criteria | Test Case ID                 |
| -------------- | --------------------------- | ---------------------------- |
| REQ-TIME-001   | AC-TIME-001                 | TIME-001                     |
| REQ-TIME-002   | AC-TIME-002                 | TIME-002                     |
| REQ-TIME-003   | AC-TIME-003                 | TIME-002                     |
| REQ-TIME-004   | AC-TIME-004                 | TIME-003                     |
| REQ-TIME-005   | AC-TIME-005                 | TIME-004                     |
| REQ-TIME-006   | AC-TIME-006                 | TIME-005                     |
| REQ-TIME-007   | AC-TIME-007                 | TIME-009, TIME-010           |
| REQ-TIME-008   | AC-TIME-008                 | TIME-006, TIME-007, TIME-008 |
| REQ-MAN-001    | AC-MAN-001                  | TIME-011                     |
| REQ-MAN-002    | AC-MAN-002                  | TIME-013, TIME-014           |
| REQ-MAN-003    | AC-MAN-003                  | TIME-012                     |
| REQ-MAN-004    | AC-MAN-004                  | TIME-011                     |
| REQ-MAN-005    | AC-MAN-005                  | TIME-015                     |

---

## Notes

Time tracking is one of the most business-critical parts of the application because incorrect time entries directly affect reports and project analysis.

Special attention should be paid to:

* correct start and stop logic
* correct duration calculation
* prevention of overlapping entries
* assignment to correct project, activity and employee
* validation of required fields
* inclusion of time entries in the final report
