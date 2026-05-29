# Test Plan

## Project: Project-Based Time Tracking Web Application

## 1. Objective

The objective of testing is to verify that the project-based time tracking web application works correctly according to the defined requirements.

The application should allow users to register, log in, work with projects, track working time, use role-based dashboards and generate reports after project completion.

The main goal of testing is to ensure that working time is recorded correctly, user roles are separated properly and final reports contain reliable project data.

---

## 2. Application Under Test

| Area                | Description                                                                          |
| ------------------- | ------------------------------------------------------------------------------------ |
| Application type    | Web application                                                                      |
| Domain              | Project-based time tracking                                                          |
| Main users          | Manager, production user, installer, personal user                                   |
| Main functionality  | Registration, login, project creation, time tracking, QR access, reports             |
| Main business value | Transparent recording and analysis of working time by project, employee and activity |

---

## 3. Scope of Testing

The following modules are included in the test scope:

* Registration with team code
* Registration without team code
* Login
* Manager dashboard
* Project creation
* Project status handling
* Start/Stop time tracking
* Manual time entry
* Production dashboard
* Installer access via QR code
* Project completion
* Report generation
* Time analysis by employee and activity
* Role-based access control

---

## 4. Out of Scope

The following areas are not included in the current test scope:

* Performance testing under high user load
* Security penetration testing
* Cross-browser testing on all available browsers
* Mobile application testing
* Payment or billing functionality
* External ERP or accounting system integration

These areas can be tested in later project phases.

---

## 5. Test Types

The testing process includes the following test types:

| Test Type                 | Purpose                                                          |
| ------------------------- | ---------------------------------------------------------------- |
| Functional testing        | Verify that application functions work according to requirements |
| Smoke testing             | Check that the most important functions work after changes       |
| Regression testing        | Verify that existing functions still work after updates          |
| UI testing                | Check layout, labels, buttons and user interaction               |
| Negative testing          | Check behavior with invalid or missing input                     |
| Role-based access testing | Verify that users see only allowed functions                     |
| End-to-end testing        | Test the complete business workflow from registration to report  |
| Data validation testing   | Verify correctness of saved and displayed data                   |

---

## 6. Test Environment

| Component        | Description                                 |
| ---------------- | ------------------------------------------- |
| Operating system | Windows                                     |
| Browser          | Google Chrome                               |
| Application      | Project-based time tracking web application |
| Backend          | Python / Flask                              |
| Frontend         | HTML, CSS, JavaScript                       |
| Database         | PostgreSQL                                  |
| Database tool    | pgAdmin                                     |
| Documentation    | Markdown                                    |
| Version control  | Git / GitHub                                |

---

## 7. Test Data

The following test data is required:

* valid manager user
* production user
* installer QR access
* valid team code
* invalid team code
* active project
* completed project
* project without time entries
* project with several time entries
* activities such as drawing, production, meeting and installation
* employees assigned to different roles

Example test data:

| Data Type         | Example                                           |
| ----------------- | ------------------------------------------------- |
| Team code         | TEAM-TEST-001                                     |
| Invalid team code | WRONG-CODE                                        |
| Manager email     | [manager@test.com](mailto:manager@test.com)       |
| Production email  | [production@test.com](mailto:production@test.com) |
| Project name      | Test Project A                                    |
| Activity          | Production                                        |
| Employee          | Max Tester                                        |

---

## 8. Entry Criteria

Testing can start when the following conditions are fulfilled:

* application is available in the test environment
* database connection works
* registration and login pages are accessible
* main application modules are implemented
* test data is prepared
* test cases are created
* tester has access to required user roles

---

## 9. Exit Criteria

Testing can be considered completed when the following conditions are fulfilled:

* all planned test cases are executed
* all critical and blocker defects are reported
* no blocker defect remains open
* smoke test is passed
* main end-to-end workflow works successfully
* test execution report is created
* known issues are documented

---

## 10. Test Approach

The testing process follows a structured approach:

1. Analyze requirements and acceptance criteria.
2. Prepare test data.
3. Execute smoke tests for the main workflow.
4. Execute functional test cases for each module.
5. Perform negative tests for invalid input and access restrictions.
6. Test role-based access for manager, production user and installer.
7. Test report generation after project completion.
8. Document defects in bug reports.
9. Create a final test execution report.

---

## 11. Main End-to-End Scenario

The main business workflow is tested as an end-to-end scenario.

```text
Registration with team code
↓
Login as manager
↓
Open manager dashboard
↓
Create new project
↓
Select activity and employee
↓
Start time tracking
↓
Stop time tracking
↓
Generate QR access for installer
↓
Installer records working time
↓
Manager completes project
↓
Manager generates final report
↓
Working time is analyzed by employee and activity
```

Expected result:

The complete workflow is executed successfully. All time entries are saved correctly and included in the final report.

---

## 12. Test Priorities

| Priority | Description                                          |
| -------- | ---------------------------------------------------- |
| High     | Business-critical functions that must work correctly |
| Medium   | Important functions that support the main workflow   |
| Low      | Minor UI or usability improvements                   |

High-priority areas:

* registration with team code
* login
* role-based access
* start/stop time tracking
* prevention of overlapping time entries
* QR access validation
* project completion
* report generation

---

## 13. Risks

| Risk                                              | Impact                           | Priority |
| ------------------------------------------------- | -------------------------------- | -------- |
| Invalid team code gives access to a team          | Unauthorized access to team data | High     |
| User sees projects from another team              | Data protection problem          | High     |
| Timer calculates wrong duration                   | Incorrect working time data      | High     |
| Overlapping time entries are possible             | Incorrect reports                | High     |
| Installer QR code does not expire                 | Unauthorized long-term access    | High     |
| Report can be generated before project completion | Incomplete report data           | High     |
| Production user can access manager functions      | Role-based access failure        | High     |
| Manual time entry accepts invalid time range      | Incorrect time data              | Medium   |

---

## 14. Defect Management

All defects found during testing are documented as bug reports.

Each bug report should include:

* bug ID
* title
* severity
* priority
* environment
* preconditions
* steps to reproduce
* actual result
* expected result
* business impact
* status
* screenshot if available

Severity levels:

| Severity | Meaning                                         |
| -------- | ----------------------------------------------- |
| Blocker  | Testing cannot continue                         |
| Critical | Main business function is broken                |
| High     | Important functionality does not work correctly |
| Medium   | Function works partly or has noticeable issue   |
| Low      | Minor UI or text issue                          |

---

## 15. Test Deliverables

The following QA artifacts are prepared for this project:

* requirements analysis
* acceptance criteria
* test plan
* manual test cases
* smoke checklist
* regression checklist
* role-based access checklist
* bug report template
* example bug reports
* test execution report

---

## 16. Test Summary

The main focus of testing is to verify that the application supports reliable project-based time tracking.

The most important quality areas are:

* correct separation of users and teams
* correct role-based access
* accurate start/stop time tracking
* secure QR-based installer access
* reliable project completion process
* correct final report generation

The application can be considered ready for further use when the main workflow works successfully and no critical defects remain open.
