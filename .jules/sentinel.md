## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2025-02-19 - Third-Party iframe security
**Vulnerability:** Third-party content embedded via `iframe` (such as YouTube videos) didn't have sandbox restrictions, posing a potential risk of unauthorized top-level navigation and XSS breakouts.
**Learning:** For defense-in-depth, even if the third party is currently trusted (like YouTube), their scripts could change. Any embedded external content requires strict boundary enforcement.
**Prevention:** Always add restrictive `sandbox` attributes (e.g., `allow-scripts allow-same-origin allow-presentation allow-popups`) to `iframe` elements to prevent XSS breakouts and unauthorized top-level navigation.
