# Bug Report BUG-002

## Title

System allows overlapping active time entries for the same employee

---

## Severity

Critical

---

## Priority

High

---

## Status

Open

---

## Environment

| Area             | Value                                       |
| ---------------- | ------------------------------------------- |
| Application      | Project-Based Time Tracking Web Application |
| Browser          | Google Chrome                               |
| Operating System | Windows                                     |
| Test Environment | Local test environment                      |
| User Role        | Manager / Production user                   |
| Module           | Start/Stop Time Tracking                    |

---

## Preconditions

* User is logged in.
* At least one project exists.
* At least one employee exists.
* At least two activities are available, for example **Zeichnung** and **Sonstige**.
* No project is completed.
* Time tracking page is available.

---

## Steps to Reproduce

1. Log in as manager.
2. Open an active project.
3. Select employee **Andreas**.
4. Select activity **Zeichnung**.
5. Click **Start**.
6. Do not click **Stop**.
7. Select the same employee **Andreas** again.
8. Select another activity, for example **Sonstige**.
9. Click **Start** again.

---

## Actual Result

The system allows another active time entry for the same employee while the first timer is still running.

As a result, the same employee can appear as working on two different activities at the same time.

---

## Expected Result

The system should prevent overlapping active time entries for the same employee.

If an employee already has an active timer, the system should block the second start attempt and display a clear validation message.

Example message:

```text
This employee already has an active time entry. Please stop the current timer before starting a new one.
```

---

## Business Impact

This defect can lead to incorrect working time data.

If one employee can work in two activities at the same time, the final report may show unrealistic project duration and incorrect distribution of working time by activity.

This can affect:

* total project time
* time per employee
* time per activity
* production time analysis
* final project report
* cost calculation and planning

For a time tracking application, this is a critical business logic issue because the accuracy of reports depends directly on correct time entries.

---

## Expected Test Evidence

Suggested screenshot:

```text
10_screenshots/bug_002_overlapping_time_entries.png
```

The screenshot should show the project history with two active or overlapping entries for the same employee.

---

## Related Test Cases

| Test Case ID     | Description                                           |
| ---------------- | ----------------------------------------------------- |
| TIME-009         | Prevent overlapping active timer for same employee    |
| TIME-010         | Prevent overlapping active timer in another activity  |
| TIME-015         | Time entry appears in report after project completion |
| REG-CHK-TIME-007 | Overlapping time entries are prevented                |

---

## Severity Explanation

Severity is **Critical** because the defect breaks the core business logic of the application. A time tracking system must not allow one employee to record parallel working time for different activities.

---

## Priority Explanation

Priority is **High** because this issue should be fixed before the application is used for real project tracking or final reporting.

---

## Suggested Fix

Before starting a new timer, the system should check whether the selected employee already has an active time entry.

Possible validation logic:

```text
If employee has active_timer = true:
    block new timer start
    show validation message
Else:
    start new timer
```
