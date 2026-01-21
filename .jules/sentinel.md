## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2025-10-28 - Bootstrap 3.3.5 XSS Vulnerability
**Vulnerability:** The project vendored Bootstrap 3.3.5 which contains multiple XSS vulnerabilities (e.g., CVE-2019-8331).
**Learning:** Legacy projects often vendor dependencies in `js/` folders, bypassing `package.json` security audits. A full upgrade to Bootstrap 5 was not feasible due to breaking changes, and upgrading jQuery to 3.x was also risky.
**Prevention:** Vendor the latest patch version of legacy libraries (e.g., Bootstrap 3.4.1) to fix security issues while maintaining compatibility.
