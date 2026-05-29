# Bug Report BUG-001

## Title

Final report is available before project completion

---

## Severity

High

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
| User Role        | Manager                                     |
| Module           | Report generation / Project completion      |

---

## Preconditions

* Manager user exists.
* Manager is logged in.
* At least one active project exists.
* Project has at least one saved time entry.
* Project status is not completed.

---

## Steps to Reproduce

1. Log in as manager.
2. Open the manager dashboard.
3. Select an active project.
4. Add or verify that at least one time entry exists.
5. Open the report section.
6. Try to generate or open the final report.

---

## Actual Result

The report can be opened or generated even though the project has not been completed yet.

---

## Expected Result

The final report should be available only after the manager clicks **“Beenden”** and the project status changes to completed.

For active or paused projects, the report button should either be disabled or a clear message should be displayed.

Example message:

```text
The final report can be generated only after project completion.
```

---

## Business Impact

This defect can lead to incorrect project analysis because the report may contain incomplete time data.

If the project is still active, additional working time can still be added by the manager, production users or installers. A report generated too early may show wrong total time, incomplete employee statistics and unreliable activity analysis.

This can affect:

* project evaluation
* internal planning
* cost calculation
* management decisions
* comparison between planned and actual work

---

## Expected Test Evidence

Suggested screenshot:

```text
10_screenshots/bug_001_report_before_completion.png
```

The screenshot should show an active project where the report is already available before project completion.

---

## Related Test Cases

| Test Case ID | Description                                         |
| ------------ | --------------------------------------------------- |
| REP-002      | Prevent report generation before project completion |
| COMP-CHK-002 | Report is available only after completion           |
| SM-021       | Manager can generate report after completion        |

---

## Severity Explanation

Severity is **High** because the defect affects a business-critical workflow. The final report is used for analysis and should be based only on completed project data.

---

## Priority Explanation

Priority is **High** because this issue should be fixed before the application is used for real project evaluation.
