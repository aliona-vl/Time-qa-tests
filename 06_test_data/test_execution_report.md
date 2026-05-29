# Test Data

## Project: Project-Based Time Tracking Web Application

## Purpose

This document defines the test data used for testing the project-based time tracking application.

Test data is required to verify registration, login, team code handling, role-based access, project creation, time tracking, QR access and report generation.

The data is fictional and used only for testing purposes.

---

## 1. Test Environment

| Area             | Value                                       |
| ---------------- | ------------------------------------------- |
| Application      | Project-Based Time Tracking Web Application |
| Environment      | Local test environment                      |
| Browser          | Google Chrome                               |
| Operating System | Windows                                     |
| Database         | PostgreSQL                                  |
| Backend          | Python / Flask                              |
| Frontend         | HTML, CSS, JavaScript                       |

---

## 2. User Roles

The application uses different user roles. Each role has different permissions.

| Role            | Description                                                                      |
| --------------- | -------------------------------------------------------------------------------- |
| Manager         | Full access to project management, QR generation, project completion and reports |
| Production user | Limited access to production-related projects and time tracking                  |
| Installer       | Temporary QR-based access to a minimalistic time tracking page                   |
| Personal user   | User registered without team code, can manage only personal projects             |

---

## 3. Test Users

| User ID  | Role            | Email                                                   | Password         | Expected Access                          |
| -------- | --------------- | ------------------------------------------------------- | ---------------- | ---------------------------------------- |
| USER-001 | Manager         | [manager@test.com](mailto:manager@test.com)             | TestPassword123! | Manager dashboard, projects, QR, reports |
| USER-002 | Production user | [production@test.com](mailto:production@test.com)       | TestPassword123! | Production dashboard and assigned tasks  |
| USER-003 | Personal user   | [personal@test.com](mailto:personal@test.com)           | TestPassword123! | Personal projects only                   |
| USER-004 | Manager Team B  | [manager.teamB@test.com](mailto:manager.teamB@test.com) | TestPassword123! | Team B projects only                     |
| USER-005 | Invalid user    | [unknown@test.com](mailto:unknown@test.com)             | WrongPassword123 | No access                                |

---

## 4. Team Codes

| Team Code ID | Team Code     | Description                   | Expected Result          |
| ------------ | ------------- | ----------------------------- | ------------------------ |
| TEAM-001     | TEAM-TEST-001 | Valid team code for Team A    | User joins Team A        |
| TEAM-002     | TEAM-TEST-002 | Valid team code for Team B    | User joins Team B        |
| TEAM-003     | WRONG-CODE    | Invalid team code             | Registration is rejected |
| TEAM-004     | EXPIRED-CODE  | Expired or inactive team code | Registration is rejected |

---

## 5. Customers

| Customer ID | Customer Name         | Description                                  |
| ----------- | --------------------- | -------------------------------------------- |
| CUST-001    | Testkunde Müller GmbH | Main test customer                           |
| CUST-002    | Beispiel Metallbau AG | Second customer for project separation tests |
| CUST-003    | Demo BauService GmbH  | Customer for report and QR tests             |

---

## 6. Employees

| Employee ID | Name              | Role / Area        | Hourly Context      |
| ----------- | ----------------- | ------------------ | ------------------- |
| EMP-001     | Andreas Schmidt   | Manager / Planning | Internal employee   |
| EMP-002     | Max Tester        | Production         | Production employee |
| EMP-003     | Anna Beispiel     | Drawing / Office   | Office employee     |
| EMP-004     | Installateur Test | Installation       | External installer  |
| EMP-005     | Maria Kontrolle   | Production         | Production employee |

---

## 7. Activities

| Activity ID | Activity    | Description                    |
| ----------- | ----------- | ------------------------------ |
| ACT-001     | Besprechung | Meeting and project discussion |
| ACT-002     | Zeichnung   | Drawing or technical planning  |
| ACT-003     | Aufmaß      | Measurement on site            |
| ACT-004     | Fertigung   | Production work                |
| ACT-005     | Montage     | Installation work              |
| ACT-006     | Sonstiges   | Other project-related work     |

---

## 8. Projects

| Project ID | Project Name                      | Team               | Customer              | Status    | Description                        |
| ---------- | --------------------------------- | ------------------ | --------------------- | --------- | ---------------------------------- |
| PROJ-001   | Test Project Active               | Team A             | Testkunde Müller GmbH | Active    | Project for time tracking tests    |
| PROJ-002   | Test Project Completed            | Team A             | Beispiel Metallbau AG | Completed | Project for report testing         |
| PROJ-003   | Test Project Without Time Entries | Team A             | Demo BauService GmbH  | Completed | Project for empty report tests     |
| PROJ-004   | Team B Project                    | Team B             | Beispiel Metallbau AG | Active    | Project for team separation tests  |
| PROJ-005   | Personal Test Project             | Personal workspace | Testkunde Müller GmbH | Active    | Project for user without team code |

---

## 9. Time Entries

| Entry ID | Project                | Employee          | Activity    | Start Time | End Time | Duration | Expected Usage      |
| -------- | ---------------------- | ----------------- | ----------- | ---------- | -------- | -------- | ------------------- |
| TIME-001 | Test Project Completed | Andreas Schmidt   | Besprechung | 08:00      | 09:00    | 60 min   | Manager time        |
| TIME-002 | Test Project Completed | Anna Beispiel     | Zeichnung   | 09:00      | 11:00    | 120 min  | Drawing time        |
| TIME-003 | Test Project Completed | Max Tester        | Fertigung   | 11:00      | 13:00    | 120 min  | Production time     |
| TIME-004 | Test Project Completed | Installateur Test | Montage     | 14:00      | 15:30    | 90 min   | Installer time      |
| TIME-005 | Test Project Active    | Max Tester        | Fertigung   | 08:00      | 10:00    | 120 min  | Active project test |

---

## 10. Manual Time Entry Test Data

| Test Data ID | Project             | Employee       | Activity       | Start Time | End Time | Expected Result    |
| ------------ | ------------------- | -------------- | -------------- | ---------- | -------- | ------------------ |
| MAN-001      | Test Project Active | Anna Beispiel  | Zeichnung      | 08:00      | 10:00    | Entry is saved     |
| MAN-002      | Test Project Active | Max Tester     | Fertigung      | 10:00      | 09:00    | Entry is rejected  |
| MAN-003      | Test Project Active | Empty employee | Fertigung      | 08:00      | 09:00    | Validation message |
| MAN-004      | Test Project Active | Max Tester     | Empty activity | 08:00      | 09:00    | Validation message |
| MAN-005      | Empty project       | Max Tester     | Fertigung      | 08:00      | 09:00    | Validation message |

---

## 11. QR Access Test Data

| QR ID  | QR Type              | Project             | User / Area | Validity    | Expected Result       |
| ------ | -------------------- | ------------------- | ----------- | ----------- | --------------------- |
| QR-001 | Production QR        | Test Project Active | Production  | Long-term   | Production page opens |
| QR-002 | Installer QR         | Test Project Active | Installer   | Temporary   | Installer page opens  |
| QR-003 | Expired Installer QR | Test Project Active | Installer   | Expired     | Access is denied      |
| QR-004 | Invalid QR           | Unknown project     | Unknown     | Invalid     | Access is denied      |
| QR-005 | Modified QR token    | Test Project Active | Installer   | Manipulated | Access is denied      |

---

## 12. Login Test Data

| Test Data ID | Email                                             | Password         | Expected Result    |
| ------------ | ------------------------------------------------- | ---------------- | ------------------ |
| LOGIN-001    | [manager@test.com](mailto:manager@test.com)       | TestPassword123! | Login successful   |
| LOGIN-002    | [production@test.com](mailto:production@test.com) | TestPassword123! | Login successful   |
| LOGIN-003    | [personal@test.com](mailto:personal@test.com)     | TestPassword123! | Login successful   |
| LOGIN-004    | [manager@test.com](mailto:manager@test.com)       | WrongPassword123 | Login rejected     |
| LOGIN-005    | [unknown@test.com](mailto:unknown@test.com)       | TestPassword123! | Login rejected     |
| LOGIN-006    | empty email                                       | TestPassword123! | Validation message |
| LOGIN-007    | [manager@test.com](mailto:manager@test.com)       | empty password   | Validation message |

---

## 13. Registration Test Data

| Test Data ID | Email                                                           | Password         | Team Code     | Expected Result               |
| ------------ | --------------------------------------------------------------- | ---------------- | ------------- | ----------------------------- |
| REG-DATA-001 | [new.team.user@test.com](mailto:new.team.user@test.com)         | TestPassword123! | TEAM-TEST-001 | User joins Team A             |
| REG-DATA-002 | [new.personal.user@test.com](mailto:new.personal.user@test.com) | TestPassword123! | Empty         | Personal workspace is created |
| REG-DATA-003 | [invalid.team.user@test.com](mailto:invalid.team.user@test.com) | TestPassword123! | WRONG-CODE    | Registration is rejected      |
| REG-DATA-004 | invalid.email                                                   | TestPassword123! | TEAM-TEST-001 | Email validation message      |
| REG-DATA-005 | [existing.user@test.com](mailto:existing.user@test.com)         | TestPassword123! | TEAM-TEST-001 | Existing user message         |

---

## 14. Report Test Data

| Report Test ID | Project                           | Time Entries                           | Expected Total Time | Expected Result                                        |
| -------------- | --------------------------------- | -------------------------------------- | ------------------- | ------------------------------------------------------ |
| REP-DATA-001   | Test Project Completed            | TIME-001, TIME-002, TIME-003, TIME-004 | 390 min             | Report shows total time correctly                      |
| REP-DATA-002   | Test Project Without Time Entries | None                                   | 0 min               | Report shows empty or zero time                        |
| REP-DATA-003   | Test Project Active               | TIME-005                               | 120 min             | Final report should not be available before completion |
| REP-DATA-004   | Team B Project                    | Team B entries only                    | Depends on entries  | Team A user cannot see this report                     |

---

## 15. Boundary and Negative Test Data

| Test Data ID | Input                               | Expected Result          |
| ------------ | ----------------------------------- | ------------------------ |
| NEG-001      | Empty required fields               | Validation message       |
| NEG-002      | Invalid email format                | Validation message       |
| NEG-003      | End time before start time          | Entry is rejected        |
| NEG-004      | Same employee starts two timers     | Second timer is rejected |
| NEG-005      | Expired QR link                     | Access is denied         |
| NEG-006      | Modified QR token                   | Access is denied         |
| NEG-007      | User opens another team project URL | Access is denied         |
| NEG-008      | Production user opens manager panel | Access is denied         |

---

## 16. Data Preparation Notes

Before test execution, the following data should be prepared:

1. At least one manager user.
2. At least one production user.
3. At least one personal user without team code.
4. Two different teams.
5. Several test projects with different statuses.
6. Several employees and activities.
7. Valid and invalid team codes.
8. Valid, expired and invalid QR links.
9. Projects with and without time entries.

---

## 17. Test Data Summary

This test data supports the following testing areas:

* registration with team code
* registration without team code
* login and logout
* role-based access
* project creation
* time tracking
* manual time entry
* QR access
* project completion
* report generation
* team data separation

The test data is designed to support positive, negative, boundary and end-to-end testing.
