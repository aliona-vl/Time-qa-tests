# Test Execution Report

## Project: Project-Based Time Tracking Web Application

## Report Purpose

This document summarizes the test execution results for the project-based time tracking web application.

The purpose of this report is to show which test areas were executed, which defects were found and whether the application is ready for further testing or release.

---

## 1. Test Summary

| Area             | Result                                      |
| ---------------- | ------------------------------------------- |
| Application      | Project-Based Time Tracking Web Application |
| Test type        | Manual functional testing                   |
| Test level       | System testing                              |
| Test approach    | Requirements-based testing                  |
| Test environment | Local test environment                      |
| Browser          | Google Chrome                               |
| Operating system | Windows                                     |
| Tester role      | QA / Software Tester                        |
| Report status    | Draft                                       |

---

## 2. Test Scope

The following modules were included in the test execution:

* registration with and without team code
* login
* manager dashboard
* project creation
* start/stop time tracking
* manual time entry
* production dashboard
* QR access for installers
* project completion
* report generation
* role-based access control
* UI checks
* regression checks

---

## 3. Test Execution Overview

| Metric                   | Result |
| ------------------------ | ------ |
| Total planned test cases | 80     |
| Executed test cases      | 65     |
| Passed test cases        | 52     |
| Failed test cases        | 4      |
| Blocked test cases       | 3      |
| Not run test cases       | 15     |
| Pass rate                | 80%    |

---

## 4. Execution Status by Area

| Test Area                   | Executed | Passed | Failed | Blocked | Status           |
| --------------------------- | -------: | -----: | -----: | ------: | ---------------- |
| Registration with team code |        8 |      7 |      1 |       0 | Partially Passed |
| Login                       |       10 |     10 |      0 |       0 | Passed           |
| Manager dashboard           |       10 |      9 |      1 |       0 | Partially Passed |
| Project creation            |       10 |     10 |      0 |       0 | Passed           |
| Time tracking               |       12 |     10 |      1 |       1 | Partially Passed |
| QR access                   |        8 |      6 |      1 |       1 | Partially Passed |
| Role-based access           |       10 |      8 |      1 |       1 | Partially Passed |
| Reports                     |        7 |      5 |      1 |       1 | Partially Passed |
| UI checks                   |       10 |      9 |      1 |       0 | Partially Passed |

---

## 5. Defects Found

| Bug ID  | Title                                                                | Severity | Priority | Status |
| ------- | -------------------------------------------------------------------- | -------- | -------- | ------ |
| BUG-001 | Final report is available before project completion                  | High     | High     | Open   |
| BUG-002 | System allows overlapping active time entries for the same employee  | Critical | High     | Open   |
| BUG-003 | Expired installer QR access is still available after expiration time | High     | High     | Open   |
| BUG-004 | Production user can see and access the Manager Panel button          | High     | High     | Open   |

---

## 6. Critical Findings

### BUG-002: Overlapping time entries

The most critical issue found during testing is that the system allows overlapping active time entries for the same employee.

This affects the core business logic of the application because one employee should not be able to work on two different activities at the same time.

Impact:

* incorrect total working time
* incorrect activity-based analysis
* incorrect employee-based analysis
* unreliable final project report

---

### BUG-004: Production user can see Manager Panel

A role-based access issue was found: the production user can see the **Manager Panel** button.

This is a high-priority issue because production users should have a limited interface and should not see manager-related functions.

Impact:

* weak role separation
* possible unauthorized access
* unclear user interface
* risk of accessing management functions

---

## 7. Test Result Details

### Registration

Registration works in the main positive scenarios. A user can register with a valid team code and can also register without team code for personal project usage.

The most important validation and data separation checks should continue to be tested, especially invalid or expired team code handling.

Result:

```text
Partially Passed
```

---

### Login

Login works correctly for valid users. Invalid credentials and empty fields are rejected.

Result:

```text
Passed
```

---

### Manager Dashboard

The manager dashboard loads correctly and shows project-related information. Project creation and project opening are available.

One issue was found in relation to role-based visibility, because production users may see manager-related elements.

Result:

```text
Partially Passed
```

---

### Project Creation

Project creation works correctly with valid data. Created projects appear on the dashboard and can be opened for time tracking.

Result:

```text
Passed
```

---

### Time Tracking

Start and stop time tracking work in the basic scenario. Time entries can be saved and assigned to project, employee and activity.

However, overlapping active time entries for the same employee are possible. This is a critical issue.

Result:

```text
Partially Passed
```

---

### QR Access

QR access works in the basic positive scenario. Installer page can be opened using QR access.

However, expired QR access must be checked strictly and should be blocked after expiration.

Result:

```text
Partially Passed
```

---

### Reports

Reports can display project-related time data. The report logic is important because it supports project analysis.

A defect was found where report generation can be available before project completion.

Result:

```text
Partially Passed
```

---

### Role-Based Access

Role-based access is partially working, but one important issue was found: production users can see the **Manager Panel** button.

Role-based access should be improved and retested.

Result:

```text
Partially Passed
```

---

## 8. Risks Remaining

| Risk                                               | Impact                                  | Priority |
| -------------------------------------------------- | --------------------------------------- | -------- |
| Overlapping time entries remain possible           | Incorrect reports and time calculations | High     |
| Production user can see manager functions          | Access control issue                    | High     |
| Report available before project completion         | Incomplete project analysis             | High     |
| Expired QR access may still work                   | Unauthorized temporary access           | High     |
| Team data separation needs full regression testing | Possible data visibility issue          | High     |

---

## 9. Recommendation

The application should not be considered fully ready for production use until the high-priority defects are fixed and retested.

Recommended next steps:

1. Fix overlapping time entry validation.
2. Hide Manager Panel button for production users.
3. Add backend role check for manager routes.
4. Block final report generation before project completion.
5. Validate QR token expiration on backend.
6. Execute regression testing after fixes.
7. Update defect statuses after retesting.

---

## 10. Exit Criteria Evaluation

| Exit Criteria                    | Status        | Comment                                    |
| -------------------------------- | ------------- | ------------------------------------------ |
| All critical test cases executed | Partially met | Some test cases are still not run          |
| No blocker defects remain open   | Met           | No blocker defects found                   |
| No critical defects remain open  | Not met       | BUG-002 is critical                        |
| Smoke test passed                | Partially met | Main workflow works, but high issues exist |
| Test execution report created    | Met           | This report documents the current status   |
| Known issues documented          | Met           | Main defects are documented                |

---

## 11. Overall Test Conclusion

The application shows a functional and promising implementation of project-based time tracking. The main workflow is understandable and several core functions are already available.

However, the current test execution found important issues in business logic, access control and reporting.

Overall test status:

```text
Partially Passed
```

The application is suitable for further testing and improvement, but the identified high-priority defects should be fixed before real business usage.

---

## 12. Retest Plan

After fixing the reported defects, the following areas should be retested:

* overlapping time entry prevention
* role-based access for production users
* visibility of Manager Panel button
* backend protection of manager routes
* QR expiration handling
* report availability after project completion
* report data accuracy

Retest result should be documented in an updated test execution report or in individual bug reports.
