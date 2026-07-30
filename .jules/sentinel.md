## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2024-05-22 - Obfuscate Email Addresses
**Vulnerability:** Information Exposure (email scraping risk via hardcoded `mailto:` links).
**Learning:** Hardcoding email addresses directly in HTML exposes them to automated spam bots. Using obfuscated text and dynamically constructing the `mailto:` link at runtime in an external JS file protects against basic scraping while adhering to strict CSP rules.
**Prevention:** Always obfuscate email addresses in source code and construct sensitive links dynamically. Ensure that when assigning DOM text to standard attributes, you properly encode the values (e.g., `encodeURIComponent`) to satisfy CodeQL constraints.
