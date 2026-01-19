## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2025-02-20 - Manifest vs. Reality Discrepancy
**Vulnerability:** Bootstrap XSS (CVE-2019-8331) persisted despite `package.json` listing a safe version (`bootstrap: ^5.1.3`).
**Learning:** In legacy "hybrid" repositories, `package.json` often only tracks build tools or unused dev dependencies, while the actual runtime assets are manually vendored in `js/` folders. Trusting the manifest led to a false sense of security.
**Prevention:** Always verify the version headers inside the actual `.js` or `.css` files served by the application, ignoring `package.json` for frontend assets unless a build pipeline is confirmed.
