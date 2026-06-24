## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2025-06-24 - DOM XSS Prevention in Dynamic Mailto Links
**Vulnerability:** Constructing `mailto:` links dynamically via `window.location.href` using unsanitized DOM data attributes (like `data-user`) risks DOM XSS if attributes are injected or maliciously reinterpreted.
**Learning:** Security scanners like CodeQL will flag unescaped dynamic URLs assigned to `window.location.href` as a critical DOM XSS vulnerability, even for seemingly harmless `mailto:` schemes derived from hardcoded HTML attributes.
**Prevention:** Always wrap dynamically extracted DOM attributes in `encodeURIComponent()` before concatenating them into navigation sinks like `window.location.href`.
