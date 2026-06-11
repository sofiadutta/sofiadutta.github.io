## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2025-06-11 - Email Obfuscation
**Vulnerability:** Plaintext email address in mailto link exposed to scraping by spam bots.
**Learning:** Exposed email addresses in static HTML are easily harvested. Obfuscating them using data attributes and constructing the link client-side provides a simple yet effective defense-in-depth measure against automated scraping, though it relies on JavaScript execution.
**Prevention:** Avoid embedding plaintext email addresses directly in `href="mailto:..."` attributes. Use dynamic construction via JavaScript or server-side obfuscation techniques to protect contact information.
