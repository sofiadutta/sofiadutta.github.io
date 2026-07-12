## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2024-05-24 - Protect Emails from Scraping Bots
**Vulnerability:** Hardcoded cleartext emails in `href="mailto:..."` leave users highly vulnerable to spam bots scraping the site.
**Learning:** We can securely de-obfuscate the email address dynamically on the client side, construct a native `mailto:` link, and add a "Copy to Clipboard" button for enhanced UX, without leaving the cleartext email in the HTML. We must use `encodeURIComponent()` to avoid DOM XSS.
**Prevention:** Avoid putting raw email strings in HTML if spam bots are a concern. Use data attributes and a hydration function instead.
