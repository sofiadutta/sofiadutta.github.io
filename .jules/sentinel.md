## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2024-05-28 - Client-side Email De-obfuscation
**Vulnerability:** Spam bots harvesting cleartext email addresses. Obfuscated emails degrade UX if left un-clickable.
**Learning:** We can maintain anti-spam obfuscation in static HTML and use JavaScript to dynamically generate an accessible `mailto:` link and copy button. When constructing dynamic URLs from DOM attributes, we must wrap them in `encodeURIComponent()` to avoid DOM XSS. For clipboard operations, we must include `.catch()` blocks for unhandled rejections in non-secure contexts.
**Prevention:** Use `document.createElement()` and `textContent` instead of string concatenation to `innerHTML` when deriving dynamic text from the DOM.
