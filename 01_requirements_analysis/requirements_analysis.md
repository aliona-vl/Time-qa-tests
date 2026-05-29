# Requirements Analysis

## Project: Project-Based Time Tracking Web Application

This document describes the main functional requirements of the project-based time tracking application and defines the QA focus for each feature.

The application is used to create projects, track working time, separate user roles and generate reports after project completion.

---

## 1. Registration with Team Code

### Requirement

A user can register with a team code in order to join an existing team.

If no team code is entered, the user can still register, but can only create and manage personal projects.

### Expected Behavior

* A valid team code allows the user to join an existing team.
* An invalid team code should be rejected.
* Registration without team code creates a personal workspace.
* Team users can work with team projects.
* Personal users cannot access team projects.
* Error messages should be displayed for invalid input.

### QA Focus

* Positive testing with valid team code
* Negative testing with invalid team code
* Registration without team code
* Data separation between team projects and personal projects
* Validation of required fields

---

## 2. Login

### Requirement

Registered users can log in to the application using valid credentials.

### Expected Behavior

* User can log in with valid email and password.
* Login with invalid credentials should be rejected.
* Empty required fields should show validation messages.
* After successful login, the user is redirected to the correct dashboard.

### QA Focus

* Successful login
* Login with wrong password
* Login with unknown email
* Login with empty fields
* Correct redirection after login

---

## 3. Manager Dashboard

### Requirement

The manager has access to a dashboard where projects can be created, opened and managed.

The dashboard is designed as a tile-based project panel.

### Expected Behavior

* Manager can see project tiles.
* Manager can create new projects.
* Manager can open an existing project.
* Project statuses are visible.
* Manager can access reports after project completion.
* Manager can generate QR access for production or installers.

### QA Focus

* Dashboard visibility for manager
* Correct display of project tiles
* Project status display
* Access to project details
* Access restriction for non-manager users

---

## 4. Project Creation

### Requirement

The manager can create a new project and define important project information.

### Expected Behavior

A project can include:

* project name
* customer
* status
* activities
* employees
* project-related time entries

After creation, the project should appear in the manager dashboard.

### QA Focus

* Create project with valid data
* Validation of required fields
* Project visibility after creation
* Correct project status
* Prevention of duplicate or incomplete project data

---

## 5. Start/Stop Time Tracking

### Requirement

Users can track working time by selecting a project, activity and employee, then starting and stopping a timer.

### Expected Behavior

* User selects a project.
* User selects an activity from the list.
* User selects an employee.
* User clicks Start.
* Timer starts successfully.
* User clicks Stop when the activity is completed.
* Time entry is saved with start time, end time and duration.

### QA Focus

* Start timer with valid data
* Stop active timer
* Correct calculation of duration
* Validation when activity is missing
* Validation when employee is missing
* Prevention of overlapping time entries
* Saving of time entry in the correct project

---

## 6. Manual Time Entry

### Requirement

In addition to the Start/Stop function, users can enter working time manually.

### Expected Behavior

* User can enter start and end time manually.
* Manual entry must be assigned to a project.
* Manual entry must include an activity and employee.
* Invalid time ranges should be rejected.

### QA Focus

* Manual entry with valid data
* End time earlier than start time
* Missing activity
* Missing employee
* Missing project
* Correct saving of manually entered time

---

## 7. Production Dashboard

### Requirement

Production users have a separate dashboard with limited access.

They can see only relevant tasks and use the Start/Stop function for their own work.

### Expected Behavior

* Production user sees only production-related tasks.
* Production user can start and stop working time.
* Production user cannot access manager data.
* Production user cannot generate reports.
* Production user cannot manage all projects.

### QA Focus

* Correct role-based access
* Limited data visibility
* Start/Stop function for production
* Access denial for manager-only functions

---

## 8. Installer QR Access

### Requirement

Installers can access a minimalistic time tracking page using a QR code provided by the manager.

The QR code for installers is valid only for a limited time.

### Expected Behavior

* Manager can generate QR access.
* Installer can open the page using a valid QR code.
* Installer sees a minimalistic page.
* Installer can track working time.
* Expired QR code should be rejected.
* Invalid QR code should be rejected.

### QA Focus

* Valid QR access
* Expired QR access
* Invalid QR access
* Minimalistic installer page
* Correct saving of installer time entries
* Security of QR-based access

---

## 9. Project Completion

### Requirement

A project can be completed by the manager.

Only after project completion should report generation and final analysis be available.

### Expected Behavior

* Manager can complete a project.
* Completed project changes its status.
* Report generation becomes available only after completion.
* Active projects should not allow final report generation.

### QA Focus

* Complete active project
* Status change after completion
* Report button visibility
* Prevention of report generation before completion
* Data consistency after project completion

---

## 10. Report Generation and Time Analysis

### Requirement

After project completion, the manager can generate a report and analyze time data.

The report should show who worked on which activity and how long each project area took.

### Expected Behavior

The report should include:

* total project time
* time by employee
* time by activity
* production time
* installer time
* project-related time entries

### QA Focus

* Report generation after completion
* Correct total time calculation
* Correct employee-based analysis
* Correct activity-based analysis
* Inclusion of production and installer time
* Data consistency between time entries and report

---

## 11. Role-Based Access

### Requirement

The application uses different roles with different permissions.

Main roles:

* Manager
* Production user
* Installer
* Personal user without team code

### Expected Behavior

* Manager has full project and report access.
* Production user has limited task access.
* Installer has QR-based minimal access.
* Personal user can manage only own projects.
* Users cannot access unauthorized data or routes.

### QA Focus

* Permission checks
* Unauthorized access attempts
* Data separation
* Correct dashboard per role
* Security of restricted functions

---

## 12. Main Risks

The most important risks for this application are:

* Incorrect team code handling
* Users seeing projects from another team
* Incorrect role-based access
* Overlapping time entries
* Incorrect time calculation
* Invalid QR code access
* Report generation before project completion
* Incorrect total time in the final report
* Missing production or installer time in reports

---

## 13. QA Summary

The application contains several business-critical workflows. The most important testing areas are registration with team code, role-based access, time tracking, QR access and report generation.

A structured QA approach is necessary because incorrect time data can lead to wrong project analysis, incorrect planning and unreliable business decisions.
