# Bug Report BUG-004

## Title

Production user can see and access the Manager Panel button

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
| User Role        | Production user                             |
| Module           | Production Dashboard / Role-Based Access    |

---

## Preconditions

* Production user exists.
* Production user is logged in.
* Production dashboard is available.
* Production user should have access only to production-related projects and time tracking.
* Manager Panel should be available only for manager users.

---

## Steps to Reproduce

1. Open the application.
2. Log in as a production user.
3. Open the production dashboard.
4. Check the visible navigation buttons and available actions.
5. Find the **Manager Panel** button.
6. Click the **Manager Panel** button.

---

## Actual Result

The **Manager Panel** button is visible for the production user.

After clicking the button, the production user can open the manager area or see manager-related functions.

This means the production user is not properly restricted to the production dashboard.

---

## Expected Result

The **Manager Panel** button should not be visible for production users.

Production users should see only production-related functions, for example:

* assigned production projects
* open project button
* start time tracking
* stop time tracking

The production user must not see or access:

* Manager Panel
* project administration
* QR generation
* reports
* project completion
* full team or management data

If the production user tries to open the manager area manually, access should be denied.

Example message:

```text
Access denied. You do not have permission to open this page.
```

---

## Business Impact

This defect breaks the role-based access concept of the application.

Production users should have a limited interface focused only on their own production tasks. If the Manager Panel button is visible, the user may access or try to access functions that are not intended for this role.

This can affect:

* confidentiality of management data
* separation of responsibilities
* project data integrity
* report reliability
* access control
* user interface clarity

The issue is especially important because the application uses different dashboards for different roles. If production users can see manager functions, the role concept is not implemented correctly.

---

## Expected Test Evidence

Suggested screenshot:

```text
10_screenshots/bug_004_production_user_can_see_manager_panel.png
```

The screenshot should show the production dashboard with the visible **Manager Panel** button.

---

## Related Test Cases

| Test Case ID  | Description                                                   |
| ------------- | ------------------------------------------------------------- |
| ROLE-006      | Production user opens production dashboard                    |
| ROLE-007      | Production user sees only production tasks                    |
| ROLE-009      | Production user cannot access manager dashboard               |
| ROLE-010      | Production user cannot generate reports                       |
| RBAC-PROD-006 | Production user cannot create manager projects                |
| RBAC-PROD-007 | Production user cannot access manager reports                 |
| RBAC-PROD-010 | Production user cannot access manager dashboard by direct URL |
| UI-PROD-004   | Manager dashboard button is visible only when allowed         |

---

## Severity Explanation

Severity is **High** because the defect affects role-based access and exposes manager-related functionality to a user with limited permissions.

Even if some manager functions are blocked later, the button itself should not be visible for the production role because it creates an incorrect user flow and indicates weak access separation.

---

## Priority Explanation

Priority is **High** because role-based access must work reliably before the application can be used in a real business environment.

Production users should not see management functions in the user interface.

---

## Suggested Fix

The visibility of the **Manager Panel** button should depend on the user role.

The button should be rendered only for users with the manager role.

Possible frontend logic:

```text
If current_user.role == "manager":
    show Manager Panel button
Else:
    hide Manager Panel button
```

However, hiding the button in the frontend is not enough. The backend must also check the user role before allowing access to the manager area.

Possible backend logic:

```text
If current_user.role != "manager":
    deny access
    redirect to allowed dashboard
Else:
    allow manager panel access
```

Both frontend and backend checks are required:

* frontend: hide unavailable functions from the user interface
* backend: prevent unauthorized access even if the URL is opened manually

---

## Retest Scenario

After the fix:

1. Log in as production user.
2. Open production dashboard.
3. Verify that the **Manager Panel** button is not visible.
4. Try to open manager dashboard URL directly.
5. Verify that access is denied.
6. Log in as manager.
7. Verify that the **Manager Panel** button is visible for manager.

Expected retest result:

```text
Production user cannot see or access Manager Panel.
Manager user can see and access Manager Panel.
```
