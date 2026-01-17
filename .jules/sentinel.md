## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2025-05-23 - Manifest vs. Reality Mismatch
**Vulnerability:** `package.json` claimed Bootstrap 5.1.3, but the actual vendored file was Bootstrap 3.3.5 (vulnerable to XSS). Additionally, `js/scripts.js` contained incompatible Bootstrap 5 code.
**Learning:** In legacy repositories, package manifests (`package.json`) are often unreliable documentation rather than the source of truth. Relying on them can mask the presence of vulnerable, outdated vendored libraries.
**Prevention:** Always verify the version of vendored libraries by inspecting the file headers (`grep -i "v[0-9]" file.js`) or content, not just the package manifest. Remove dead/incompatible code immediately to clarify the attack surface.
