## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2025-02-19 - Dynamic Email De-obfuscation
**Vulnerability:** Hardcoded cleartext emails in HTML source or easily decodable DOM structures are susceptible to spam bot harvesting, defeating anti-spam measures.
**Learning:** Obfuscating emails in static HTML (like using 'DOT' and 'AT') is effective, but converting them back to cleartext links via hardcoded replacements in the source defeats the purpose.
**Prevention:** Maintain obfuscated text in HTML and dynamically reconstruct it into native `mailto:` links with client-side JavaScript, ensuring proper DOM XSS protections using `encodeURIComponent()` (with `%40` handled for email clients) and safe DOM insertion via `textContent` and `document.createElement()`.
