## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2025-02-19 - Email Harvester Protection
**Vulnerability:** Email addresses hardcoded into HTML `mailto:` links are trivial for bots and scrapers to harvest, resulting in spam.
**Learning:** Hardcoded emails expose the user's direct contact information to automated scraping tools.
**Prevention:** Obfuscate the email by removing the direct `href="mailto:..."` link. Store email parts in `data-*` attributes (`data-user`, `data-domain`) and use a click event listener to dynamically assemble and navigate to the `mailto:` URL.
