# UI Test Checklist

## Project: Project-Based Time Tracking Web Application

## Purpose

This checklist is used to verify the user interface of the project-based time tracking web application.

The goal of UI testing is to ensure that pages, forms, buttons, navigation elements, colors, text labels and layouts are displayed correctly and support clear user interaction.

---

## Test Object

Project-based time tracking web application.

---

## UI Test Scope

The UI test covers the following screens:

* start page / login page
* registration tab
* manager dashboard
* project cards
* project detail page
* start/stop time tracking page
* manual time entry
* QR modal
* production dashboard
* report page
* mobile/tablet layout

---

## Related Screenshots

| Screenshot                   | Screen                            |
| ---------------------------- | --------------------------------- |
| `02-startseite.png`          | Login / start page                |
| `03-login.png`               | Login with entered credentials    |
| `04-dashboard.png`           | Manager dashboard                 |
| `05-projektuebersicht.png`   | Project detail / time tracking    |
| `07-start-zeiterfassung.png` | Start time tracking               |
| `08-stop-zeiterfassung.png`  | Stop time tracking / manual entry |
| `09-beenden.png`             | Project completion                |
| `10-bericht.png`             | Project report                    |
| `11-fertigung.png`           | Production dashboard              |
| `12-qr.png`                  | QR modal                          |
| `dashboard-landscape(1).png` | Tablet / landscape view           |

---

## General UI Checklist

| ID     | Check                                      | Expected Result                                                       | Priority | Status  |
| ------ | ------------------------------------------ | --------------------------------------------------------------------- | -------- | ------- |
| UI-001 | Application uses consistent dark theme     | Colors and layout are visually consistent across pages.               | Medium   | Not Run |
| UI-002 | Main buttons are clearly visible           | Primary action buttons are easy to find.                              | High     | Not Run |
| UI-003 | Labels are readable                        | Text labels are readable and not cut off.                             | High     | Not Run |
| UI-004 | Input fields are clearly recognizable      | Input fields are visible and usable.                                  | High     | Not Run |
| UI-005 | Buttons have clear text                    | Button labels describe the action correctly.                          | High     | Not Run |
| UI-006 | Page spacing is consistent                 | Elements are not too close or overlapping.                            | Medium   | Not Run |
| UI-007 | Important actions are visually highlighted | Start, Stop, Save, Generate QR and Finish buttons are visually clear. | High     | Not Run |
| UI-008 | Error and validation messages are visible  | User can clearly see what went wrong.                                 | High     | Not Run |
| UI-009 | Navigation elements are easy to find       | User can move between dashboard, project, report and QR areas.        | High     | Not Run |
| UI-010 | Layout does not break on smaller screens   | Content remains usable on tablet or reduced screen width.             | High     | Not Run |

---

## Login and Registration UI

| ID         | Check                                  | Expected Result                                    | Priority | Status  |
| ---------- | -------------------------------------- | -------------------------------------------------- | -------- | ------- |
| UI-LOG-001 | Login tab is visible                   | User can clearly see the login area.               | High     | Not Run |
| UI-LOG-002 | Registration tab is visible            | User can switch to registration.                   | High     | Not Run |
| UI-LOG-003 | E-mail field is visible and labeled    | User understands where to enter e-mail.            | High     | Not Run |
| UI-LOG-004 | Password field is visible and labeled  | User understands where to enter password.          | High     | Not Run |
| UI-LOG-005 | Login button is clearly visible        | Login action is easy to identify.                  | High     | Not Run |
| UI-LOG-006 | Password reset button is visible       | User can find password reset option.               | Medium   | Not Run |
| UI-LOG-007 | Text about team code is understandable | User understands login behavior without team code. | Medium   | Not Run |
| UI-LOG-008 | Input focus is visually clear          | Active input field is visually highlighted.        | Medium   | Not Run |

---

## Manager Dashboard UI

| ID          | Check                                    | Expected Result                                                      | Priority | Status  |
| ----------- | ---------------------------------------- | -------------------------------------------------------------------- | -------- | ------- |
| UI-DASH-001 | Logged-in user is displayed              | User email is visible in the header.                                 | Medium   | Not Run |
| UI-DASH-002 | Logout button is visible                 | User can log out easily.                                             | High     | Not Run |
| UI-DASH-003 | Project name input is visible            | User can enter a new project name.                                   | High     | Not Run |
| UI-DASH-004 | Customer selection field is visible      | User can select a customer for a project.                            | High     | Not Run |
| UI-DASH-005 | “Create new project” button is visible   | Project creation action is clear.                                    | High     | Not Run |
| UI-DASH-006 | Navigation buttons are visible           | Employees, customers, report and QR buttons are displayed.           | High     | Not Run |
| UI-DASH-007 | Project status colors are understandable | Active, running, paused and completed projects can be distinguished. | High     | Not Run |
| UI-DASH-008 | Project cards display key information    | Project name, customer, status and total time are visible.           | High     | Not Run |
| UI-DASH-009 | Edit button on project card is visible   | User can open project for editing or tracking.                       | High     | Not Run |
| UI-DASH-010 | Project counters are visible             | Total, active and completed project numbers are displayed.           | Medium   | Not Run |

---

## Project Detail and Time Tracking UI

| ID          | Check                                           | Expected Result                                  | Priority | Status  |
| ----------- | ----------------------------------------------- | ------------------------------------------------ | -------- | ------- |
| UI-TIME-001 | Project name is displayed                       | User knows which project is open.                | High     | Not Run |
| UI-TIME-002 | Customer name is displayed                      | Project customer is visible.                     | Medium   | Not Run |
| UI-TIME-003 | Created date/time is displayed                  | Project metadata is visible.                     | Low      | Not Run |
| UI-TIME-004 | Total time is visible                           | Current project total time is displayed clearly. | High     | Not Run |
| UI-TIME-005 | Employee dropdown is visible                    | User can select employee.                        | High     | Not Run |
| UI-TIME-006 | Activity dropdown is visible                    | User can select activity.                        | High     | Not Run |
| UI-TIME-007 | Start button is clearly visible                 | User can start time tracking easily.             | High     | Not Run |
| UI-TIME-008 | Stop button is clearly visible for active entry | User can stop active timer.                      | High     | Not Run |
| UI-TIME-009 | Manual duration field is visible                | User can enter duration manually.                | Medium   | Not Run |
| UI-TIME-010 | Save button for manual entry is visible         | User can save manual time entry.                 | Medium   | Not Run |
| UI-TIME-011 | Project history section is readable             | User can see previous time entries.              | High     | Not Run |
| UI-TIME-012 | Back button is visible                          | User can return to dashboard.                    | High     | Not Run |
| UI-TIME-013 | Finish project button is visible                | Manager can complete project.                    | High     | Not Run |
| UI-TIME-014 | Active timer entry is visually highlighted      | Running work session is easy to recognize.       | High     | Not Run |

---

## QR Modal UI

| ID        | Check                           | Expected Result                        | Priority | Status  |
| --------- | ------------------------------- | -------------------------------------- | -------- | ------- |
| UI-QR-001 | QR modal opens correctly        | Modal is displayed above current page. | High     | Not Run |
| UI-QR-002 | QR code is clearly visible      | QR code can be scanned.                | High     | Not Run |
| UI-QR-003 | QR link is visible              | Link is displayed for manual use.      | Medium   | Not Run |
| UI-QR-004 | Copy link button is visible     | User can copy QR link.                 | Medium   | Not Run |
| UI-QR-005 | Kiosk open button is visible    | User can open kiosk page.              | Medium   | Not Run |
| UI-QR-006 | PNG save button is visible      | User can save QR code as PNG.          | Medium   | Not Run |
| UI-QR-007 | Print button is visible         | User can print QR code.                | Medium   | Not Run |
| UI-QR-008 | Close button is visible         | User can close modal.                  | High     | Not Run |
| UI-QR-009 | QR generation button is visible | User can generate new QR code.         | High     | Not Run |

---

## Report UI

| ID         | Check                             | Expected Result                                                | Priority | Status  |
| ---------- | --------------------------------- | -------------------------------------------------------------- | -------- | ------- |
| UI-REP-001 | Report title is visible           | Project report title is displayed.                             | High     | Not Run |
| UI-REP-002 | Customer name is visible          | Report shows related customer.                                 | Medium   | Not Run |
| UI-REP-003 | Total time badges are visible     | Total time values are easy to identify.                        | High     | Not Run |
| UI-REP-004 | Manager panel section is visible  | Manager times are displayed separately.                        | High     | Not Run |
| UI-REP-005 | Production section is visible     | Production times are displayed separately.                     | High     | Not Run |
| UI-REP-006 | Installation section is visible   | Installation times are displayed separately.                   | High     | Not Run |
| UI-REP-007 | Total section is visible          | Summary of all areas is displayed.                             | High     | Not Run |
| UI-REP-008 | Project history table is readable | Date, start, end, employee, activity and duration are visible. | High     | Not Run |
| UI-REP-009 | Print button is visible           | User can print report.                                         | Medium   | Not Run |
| UI-REP-010 | Back button is visible            | User can return to previous page.                              | Medium   | Not Run |

---

## Production Dashboard UI

| ID          | Check                                                 | Expected Result                                    | Priority | Status  |
| ----------- | ----------------------------------------------------- | -------------------------------------------------- | -------- | ------- |
| UI-PROD-001 | Production dashboard title is visible                 | User understands that production area is open.     | High     | Not Run |
| UI-PROD-002 | Project cards are visible                             | Production user can see assigned projects.         | High     | Not Run |
| UI-PROD-003 | Open button is visible on project cards               | User can open assigned project.                    | High     | Not Run |
| UI-PROD-004 | Manager dashboard button is visible only when allowed | Unauthorized users should not access manager area. | High     | Not Run |
| UI-PROD-005 | Layout is usable on tablet screen                     | Cards and buttons remain readable and clickable.   | High     | Not Run |

---

## Responsive / Tablet UI

| ID          | Check                                    | Expected Result                                    | Priority | Status  |
| ----------- | ---------------------------------------- | -------------------------------------------------- | -------- | ------- |
| UI-RESP-001 | Dashboard is usable in landscape mode    | Project cards and controls fit the screen.         | High     | Not Run |
| UI-RESP-002 | Buttons are large enough for touch input | User can tap buttons on tablet.                    | High     | Not Run |
| UI-RESP-003 | Text remains readable on tablet          | Project names, times and labels are readable.      | High     | Not Run |
| UI-RESP-004 | No important controls are hidden         | User can access main functions.                    | High     | Not Run |
| UI-RESP-005 | Scroll behavior works correctly          | User can scroll through project lists and history. | Medium   | Not Run |

---

## UI Testing Notes

The application uses a dark visual style with green action buttons and colored project cards. This provides a clear visual identity, but it is important to test readability, contrast and consistency across all main screens.

Special attention should be paid to:

* readability of white text on dark background
* contrast of yellow and green project cards
* visibility of active buttons
* clarity of status colors
* usability on tablet screens
* correct display of report tables
* QR modal usability
