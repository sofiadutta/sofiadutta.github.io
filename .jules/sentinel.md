## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2025-02-19 - Safe jQuery Upgrade with Legacy Bootstrap
**Vulnerability:** Outdated jQuery v2.1.4 (XSS risks) was used with Bootstrap v3.3.5.
**Learning:** Contrary to common expectation that Bootstrap 3.x breaks with jQuery 3.x (due to `.load()`, `.error()`, etc.), this specific implementation of Bootstrap 3.3.5 and the limited set of plugins (`flexslider`, `waypoints`) functioned correctly with jQuery 3.7.1. Verification of critical UI components (sliders, scrollspy) confirmed compatibility.
**Prevention:** Always verify upgrades with functional tests (e.g. Playwright) rather than assuming incompatibility based on major version numbers.
