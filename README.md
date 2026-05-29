# Time QA Tests

## QA Portfolio for Project-Based Time Tracking Application

This repository contains QA documentation and test artifacts for a web application for project-based time tracking.

The application allows users to register with a team code, work in teams, create projects, track working time with a start/stop function, use different role-based dashboards, generate QR access for installers and create reports after project completion.

---

## Repository Purpose

The purpose of this repository is to demonstrate a structured QA process for a real time-tracking application.

This repository includes:

- requirements analysis
- acceptance criteria
- test plan
- manual test cases
- smoke and regression checklists
- role-based access testing
- QR access testing
- bug reports
- test execution reports

---

## Application Under Test

| Area | Description |
|---|---|
| Application type | Web application |
| Domain | Project-based time tracking |
| Main purpose | Digital recording and analysis of working time |
| Users | Manager, production employee, installer |
| Main functionality | Project creation, time tracking, QR access, reporting |

---

## Tested Modules

The following modules are covered by the QA documentation:

- Registration with team code
- Login
- Manager dashboard
- Project creation
- Start/Stop time tracking
- Manual time entry
- Production dashboard
- Installer access via QR code
- Project completion
- Report generation
- Time analysis by employee and activity

---

## QA Scope

The testing process focuses on verifying that the application works correctly from the user and business perspective.

Main testing areas:

- functional testing
- UI testing
- smoke testing
- regression testing
- negative testing
- role-based access testing
- end-to-end workflow testing
- report validation

---

## Tools and Technologies

| Area | Tools |
|---|---|
| Test documentation | Markdown |
| Test design | Test cases, checklists |
| Bug reporting | Markdown / GitHub Issues |
| API testing | Postman |
| Automation | Python, PyTest, Selenium |
| Database checks | PostgreSQL / pgAdmin |
| Version control | Git / GitHub |

---

## Repository Structure

```text
Time-qa-tests/
│
├── README.md
│
├── 01_requirements_analysis/
│   ├── requirements_analysis.md
│   └── acceptance_criteria.md
│
├── 02_test_plan/
│   └── test_plan.md
│
├── 03_test_cases/
│   ├── test_cases_registration_teamcode.md
│   ├── test_cases_login.md
│   ├── test_cases_manager_dashboard.md
│   ├── test_cases_project_creation.md
│   ├── test_cases_time_tracking.md
│   ├── test_cases_roles.md
│   ├── test_cases_qr_access.md
│   └── test_cases_reports.md
│
├── 04_checklists/
│   ├── smoke_test_checklist.md
│   ├── regression_test_checklist.md
│   ├── ui_test_checklist.md
│   └── role_based_access_checklist.md
│
├── 05_bug_reports/
│   ├── bug_report_template.md
│   ├── bug_001_invalid_teamcode.md
│   ├── bug_002_report_before_project_completion.md
│   └── bug_003_overlapping_time_entries.md
│
├── 06_test_data/
│   └── test_data.md
│
├── 07_api_testing/
│   └── api_test_cases.md
│
├── 08_automation_tests/
│   ├── pytest/
│   └── selenium/
│
├── 09_test_reports/
│   ├── test_execution_report.md
│   ├── smoke_test_report.md
│   └── regression_test_report.md
│
└── 10_screenshots/