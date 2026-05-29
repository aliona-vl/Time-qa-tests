# Bug Report BUG-003

## Title

Expired installer QR access is still available after expiration time

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
| User Role        | Installer / QR user                         |
| Module           | QR Access / Installer Time Tracking         |

---

## Preconditions

* Manager user exists.
* Manager is logged in.
* Active project exists.
* Temporary QR access for installer was generated.
* QR code has a defined expiration time.
* Expiration time has already passed.

---

## Steps to Reproduce

1. Log in as manager.
2. Open an active project.
3. Generate a temporary QR code for installer access.
4. Save or copy the generated QR link.
5. Wait until the QR code expiration time has passed.
6. Open the expired QR link in a browser.
7. Try to access the installer time tracking page.
8. Try to start time tracking.

---

## Actual Result

The expired QR link still opens the installer time tracking page.

The installer can still access the project and use the time tracking function after the QR code should already be expired.

---

## Expected Result

The system should reject expired QR access.

After expiration, the QR link should no longer open the installer page. The system should display a clear message.

Example message:

```text
This QR access link has expired. Please request a new QR code from the manager.
```

The installer should not be able to start or stop time tracking with an expired QR code.

---

## Business Impact

This defect can lead to unauthorized access to project-related time tracking.

Installer QR access is intended to be temporary. If an expired QR code remains valid, external or temporary users may continue to access the project longer than allowed.

This can affect:

* access control
* project data security
* correctness of time entries
* trust in QR-based access
* separation between internal and temporary users

For a time tracking application with role-based access, this is a serious security and business logic issue.

---

## Expected Test Evidence

Suggested screenshot:

```text
10_screenshots/bug_003_expired_qr_access.png
```

The screenshot should show that the installer page is still accessible after the QR code expiration time.

---

## Related Test Cases

| Test Case ID | Description                                    |
| ------------ | ---------------------------------------------- |
| QR-008       | Installer QR code expires after defined period |
| QR-009       | Invalid QR code is rejected                    |
| QR-010       | QR user cannot open manager dashboard          |
| RBAC-INS-009 | Expired installer QR code is rejected          |
| QR-CHK-003   | Expired QR code is rejected                    |

---

## Severity Explanation

Severity is **High** because the defect affects access control. A temporary QR access link must not remain valid after its expiration time.

---

## Priority Explanation

Priority is **High** because expired QR access can allow unauthorized use of the application and should be fixed before real external users or installers use the system.

---

## Suggested Fix

Before opening the QR-based installer page, the system should check whether the QR token is still valid.

Possible validation logic:

```text
If qr_token.expiration_time < current_time:
    deny access
    show expiration message
Else:
    allow access to assigned project only
```

Additionally, expired QR tokens should not allow API actions such as starting or stopping time tracking.
