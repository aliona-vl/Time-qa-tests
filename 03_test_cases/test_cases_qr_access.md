# Test Cases: QR Access

## Project: Project-Based Time Tracking Web Application

## Test Object

QR-based access for production users and installers.

## Test Basis

* Manager can generate QR access.
* Production users can receive long-term QR access.
* Installers can receive temporary QR access.
* Installer QR access is valid only for a limited period.
* QR access opens a minimalistic time tracking page.
* Users with QR access can track time only for assigned projects or tasks.
* Invalid or expired QR codes must be rejected.
* QR users must not access manager functions.

---

## Test Conditions

| ID          | Test Condition                                   | Priority |
| ----------- | ------------------------------------------------ | -------- |
| TCND-QR-001 | Manager generates QR access                      | High     |
| TCND-QR-002 | Valid QR code opens correct page                 | High     |
| TCND-QR-003 | Installer QR code expires after defined time     | High     |
| TCND-QR-004 | Invalid QR code is rejected                      | High     |
| TCND-QR-005 | QR user can track working time                   | High     |
| TCND-QR-006 | QR user cannot access manager functions          | High     |
| TCND-QR-007 | QR access is limited to assigned project or task | High     |

---

## Test Data

| Data Type            | Example                                     |
| -------------------- | ------------------------------------------- |
| Manager user         | [manager@test.com](mailto:manager@test.com) |
| Project              | Test Project A                              |
| Production QR code   | Long-term QR link                           |
| Installer QR code    | Temporary QR link                           |
| Invalid QR code      | Invalid or modified QR link                 |
| Expired QR code      | QR link after expiration date               |
| Activity             | Installation                                |
| Employee / installer | Installer Test User                         |

---

## Test Cases

| Test Case ID | Test Condition                                      | Preconditions                                           | Test Steps                                                                                                                 | Test Data                | Expected Result                                                                                 | Priority | Status  |
| ------------ | --------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------- | -------- | ------- |
| QR-001       | Manager generates QR access for production          | Manager is logged in and project exists                 | 1. Open manager dashboard. <br> 2. Open project. <br> 3. Select QR access option for production. <br> 4. Generate QR code. | Project: Test Project A  | Long-term QR access for production is generated successfully.                                   | High     | Not Run |
| QR-002       | Manager generates QR access for installer           | Manager is logged in and project exists                 | 1. Open manager dashboard. <br> 2. Open project. <br> 3. Select QR access option for installer. <br> 4. Generate QR code.  | Project: Test Project A  | Temporary QR access for installer is generated successfully.                                    | High     | Not Run |
| QR-003       | Open valid installer QR code                        | Valid installer QR code exists                          | 1. Open QR link in browser.                                                                                                | Valid installer QR link  | Minimalistic installer time tracking page is displayed.                                         | High     | Not Run |
| QR-004       | Open valid production QR code                       | Valid production QR code exists                         | 1. Open QR link in browser.                                                                                                | Valid production QR link | Production time tracking page is displayed.                                                     | High     | Not Run |
| QR-005       | Installer starts time tracking via QR page          | Installer QR page is open                               | 1. Open valid installer QR link. <br> 2. Select or confirm activity. <br> 3. Click Start.                                  | Activity: Installation   | Time tracking starts successfully.                                                              | High     | Not Run |
| QR-006       | Installer stops time tracking via QR page           | Active installer timer exists                           | 1. Click Stop.                                                                                                             | Active timer             | Time tracking stops and time entry is saved.                                                    | High     | Not Run |
| QR-007       | Installer time entry is assigned to correct project | Installer time entry was created                        | 1. Log in as manager. <br> 2. Open related project. <br> 3. Check time entries.                                            | Test Project A           | Installer time entry is visible in the correct project.                                         | High     | Not Run |
| QR-008       | Installer QR code expires after defined period      | Temporary QR code exists and expiration time has passed | 1. Open expired QR link.                                                                                                   | Expired QR link          | Access is rejected. Expiration message or access denied page is displayed.                      | High     | Not Run |
| QR-009       | Invalid QR code is rejected                         | Invalid QR link exists                                  | 1. Open invalid or modified QR link.                                                                                       | Invalid QR link          | Access is rejected.                                                                             | High     | Not Run |
| QR-010       | QR user cannot open manager dashboard               | QR user has access only through QR page                 | 1. Open valid QR page. <br> 2. Try to open manager dashboard URL.                                                          | QR user                  | Access is denied or user is redirected.                                                         | High     | Not Run |
| QR-011       | QR user cannot generate report                      | QR user has access only through QR page                 | 1. Open valid QR page. <br> 2. Try to open report URL directly.                                                            | QR user                  | Access is denied.                                                                               | High     | Not Run |
| QR-012       | QR access is limited to assigned project            | QR code is generated for Project A                      | 1. Open QR link for Project A. <br> 2. Try to access Project B using the same QR token or modified URL.                    | Project A / Project B    | Access to Project B is denied.                                                                  | High     | Not Run |
| QR-013       | QR page works without full user login               | Valid installer QR code exists                          | 1. Open browser in private mode. <br> 2. Open valid QR link.                                                               | Valid QR link            | Minimalistic QR page is accessible without normal login but only within allowed QR permissions. | High     | Not Run |
| QR-014       | QR page shows only required controls                | Valid installer QR page is open                         | 1. Open QR page. <br> 2. Check visible buttons and fields.                                                                 | Installer QR page        | Only minimal time tracking controls are visible. No manager functions are displayed.            | Medium   | Not Run |

---

## Negative Test Cases

| Test Case ID | Scenario                                    | Expected Result   |
| ------------ | ------------------------------------------- | ----------------- |
| NEG-QR-001   | Expired installer QR code is opened         | Access is denied. |
| NEG-QR-002   | Invalid QR code is opened                   | Access is denied. |
| NEG-QR-003   | QR user opens manager dashboard URL         | Access is denied. |
| NEG-QR-004   | QR user opens report URL                    | Access is denied. |
| NEG-QR-005   | QR token is modified manually               | Access is denied. |
| NEG-QR-006   | QR code for Project A is used for Project B | Access is denied. |

---

## Traceability Matrix

| Requirement ID | Related Acceptance Criteria | Test Case ID           |
| -------------- | --------------------------- | ---------------------- |
| REQ-QR-001     | AC-QR-001                   | QR-001, QR-002         |
| REQ-QR-002     | AC-QR-002                   | QR-003, QR-004         |
| REQ-QR-003     | AC-QR-003                   | QR-014                 |
| REQ-QR-004     | AC-QR-004                   | QR-005, QR-006, QR-007 |
| REQ-QR-005     | AC-QR-005                   | QR-008                 |
| REQ-QR-006     | AC-QR-006                   | QR-009                 |
| REQ-QR-007     | AC-QR-007                   | QR-012                 |
| REQ-ROLE-001   | AC-ROLE-003, AC-ROLE-005    | QR-010, QR-011         |

---

## Notes

QR access is a critical area because it provides simplified access without a full user login. Therefore, the access must be limited, controlled and secure.

Special attention should be paid to:

* expiration of installer QR codes
* difference between long-term production QR and temporary installer QR
* project-specific QR restrictions
* invalid or manipulated QR links
* prevention of access to manager functions
* correct saving of QR-based time entries
