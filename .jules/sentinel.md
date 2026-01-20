## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2026-01-20 - Attack Surface Reduction via Dead Code Removal
**Vulnerability:** Unused JavaScript files (`js/google_map.js`, `js/scripts.js`) containing insecure patterns (missing API keys) and incompatible code (Bootstrap 5 logic in Bootstrap 3 app).
**Learning:** Legacy projects often accumulate "ghost" files that are not referenced but present a risk if mistakenly used or indexed. `js/scripts.js` was actively misleading by containing valid-looking but incompatible code.
**Prevention:** Regularly audit the codebase for unreferenced files and remove them to prevent confusion and accidental inclusion of vulnerable code.
