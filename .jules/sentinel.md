## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2025-02-24 - Email Harvesting Prevention via Data Attributes
**Vulnerability:** Exposed raw `mailto:` link in `index.html` allowing easy email scraping by bots.
**Learning:** Using `data-*` attributes for email parts (user, domain) and reconstructing the link via JavaScript `window.location.href` is a simple, effective way to obfuscate emails without needing complex encoding or server-side rendering. This respects the `self` CSP while preventing static analysis scraping.
**Prevention:** Avoid raw `mailto:` links for public emails. Use the `js-email-protect` pattern with `data-user` and `data-domain` attributes.
