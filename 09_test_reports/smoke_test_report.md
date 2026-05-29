# Smoke Test Report

## Project: Project-Based Time Tracking Web Application

## Report Purpose

This document summarizes the smoke test execution for the project-based time tracking web application.

Smoke testing was performed to verify that the most important application functions are available and stable enough for further detailed testing.

---

## 1. Test Summary

| Area             | Value                  |
| ---------------- | ---------------------- |
| Test type        | Smoke testing          |
| Test level       | System testing         |
| Test environment | Local test environment |
| Browser          | Google Chrome          |
| Operating system | Windows                |
| Tester role      | QA / Software Tester   |
| Test status      | Partially Passed       |

---

## 2. Smoke Test Scope

The smoke test covered the most important business functions:

* application start page
* registration
* login
* manager dashboard
* project creation
* project opening
* start/stop time tracking
* production dashboard
* QR access
* project completion
* report generation
* logout

---

## 3. Smoke Test Execution Results

| ID     | Check                                           | Expected Result                              | Actual Result                      | Status |
| ------ | ----------------------------------------------- | -------------------------------------------- | ---------------------------------- | ------ |
| SM-001 | Application opens successfully                  | Start page is displayed without server error | Start page was displayed           | Passed |
| SM-002 | Registration page opens                         | Registration form is displayed               | Registration tab was available     | Passed |
| SM-003 | User can register with valid team code          | User is registered and assigned to team      | Registration was successful        | Passed |
| SM-004 | User can register without team code             | User receives personal workspace             | Personal registration worked       | Passed |
| SM-005 | Login page opens                                | Login form is displayed                      | Login form was displayed           | Passed |
| SM-006 | Manager can log in                              | Manager dashboard is displayed               | Manager dashboard was displayed    | Passed |
| SM-007 | Production user can log in                      | Production dashboard is displayed            | Production dashboard was displayed | Passed |
| SM-008 | Manager dashboard loads correctly               | Project overview is displayed                | Dashboard loaded successfully      | Passed |
| SM-009 | Manager can create a new project                | Project is saved successfully                | Project was created                | Passed |
| SM-010 | Created project appears on dashboard            | Project is visible after creation            | Project appeared on dashboard      | Passed |
| SM-011 | Manager can open project details                | Project detail page opens                    | Project detail page opened         | Passed |
| SM-012 | User can start time tracking                    | Timer starts successfully                    | Timer started                      | Passed |
| SM-013 | User can stop time tracking                     | Timer stops and entry is saved               | Time entry was saved               | Passed |
| SM-014 | Saved time entry is visible in project          | Entry appears in project history             | Entry was visible                  | Passed |
| SM-015 | Production dashboard opens                      | Production projects are displayed            | Production dashboard opened        | Passed |
| SM-016 | Production user cannot access manager functions | Manager functions are hidden or blocked      | Manager Panel button was visible   | Failed |
| SM-017 | Manager can generate QR access                  | QR code or link is generated                 | QR modal was displayed             | Passed |
| SM-018 | Valid installer QR link opens minimal page      | Installer page is displayed                  | QR page opened                     | Passed |
| SM-019 | Installer can track time through QR page        | Installer time entry is saved                | Basic QR workflow worked           | Passed |
| SM-020 | Manager can complete project                    | Project status changes to completed          | Project could be completed         | Passed |
| SM-021 | Manager can generate report after completion    | Final report is generated                    | Report was generated               | Passed |
| SM-022 | Report shows total project time                 | Total time is displayed                      | Total time was visible             | Passed |
| SM-023 | Logout works correctly                          | User is logged out                           | Logout worked                      | Passed |

---

## 4. Smoke Test Result

| Metric       | Result |
| ------------ | ------ |
| Total checks | 23     |
| Passed       | 22     |
| Failed       | 1      |
| Blocked      | 0      |
| Not Run      | 0      |
| Pass rate    | 95.65% |

---

## 5. Failed Smoke Check

### SM-016: Production user cannot access manager functions

Expected result:

```text
Manager functions should be hidden or blocked for production users.
```

Actual result:

```text
Production user can see the Manager Panel button.
```

Related bug report:

```text
BUG-004: Production user can see and access the Manager Panel button
```

---

## 6. Smoke Test Conclusion

The smoke test result is **Partially Passed**.

Most critical application functions are available and can be used:

* login works
* manager dashboard opens
* project creation works
* time tracking can be started and stopped
* QR modal opens
* report page is available
* logout works

However, one high-priority role-based access issue was found: the production user can see the **Manager Panel** button. This should be fixed and retested.

---

## 7. Recommendation

The application is stable enough for further functional and regression testing, but role-based access should be corrected before real business usage.

Recommended next steps:

1. Hide the Manager Panel button for production users.
2. Add backend role validation for manager routes.
3. Retest role-based access.
4. Execute regression testing after the fix.
