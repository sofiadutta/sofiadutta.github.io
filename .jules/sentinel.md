## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2026-07-23 - Anti-spam Email Obfuscation Enhancement
**Vulnerability:** Email addresses in clear text are prone to scraping by spambots, and hardcoded `mailto:` links provide easy extraction vectors.
**Learning:** Obfuscation using strings like " DOT " and " AT " deters simple scrapers but degrades user experience. It's possible to de-obfuscate this dynamically via JS and reconstruct a secure `mailto:` link without risking XSS or losing the anti-spam benefits on the source code level.
**Prevention:** Rather than writing clear-text emails or using basic `href="mailto:..."`, implement robust client-side de-obfuscation paired with a "Copy to Clipboard" utility. Use explicit `document.createElement`, `encodeURIComponent`, and block-scoped variables (`let`, `const`) inside loops for event handlers to prevent closure-related bugs.
