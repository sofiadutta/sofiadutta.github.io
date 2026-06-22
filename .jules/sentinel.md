## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2024-06-22 - Email Obfuscation
**Vulnerability:** Plaintext email addresses in source code are vulnerable to automated scraping by spam bots.
**Learning:** Hardcoding `mailto:` with cleartext emails exposes users to spam. Client-side reconstruction via data attributes combined with encodeURIComponent for the mailto scheme prevents simple regex scraping while maintaining usability.
**Prevention:** Avoid plaintext email addresses in HTML or JS. Use data attributes (e.g. `data-user`, `data-domain`) and reconstruct them dynamically on the client side.
