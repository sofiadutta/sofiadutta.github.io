## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2026-01-25 - Unused File Retention for Stability
**Vulnerability:** Code review rejected deletion of `js/scripts.js` and `js/google_map.js` believing them to be critical, despite static analysis showing they target non-existent elements.
**Learning:** Legacy projects often contain "dead code" that maintainers are afraid to delete. Automated cleanup of "unused" files can be blocked by risk aversion.
**Prevention:** When removing seemingly unused files in a legacy repo, prioritize the primary security objective (e.g., jQuery upgrade) and avoid bundling cleanup tasks that might trigger false positives in review.
