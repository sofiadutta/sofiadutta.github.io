## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2025-02-19 - Anti-Spam Email Protection Pattern
**Vulnerability:** Cleartext email addresses (mailto: links) exposed in static HTML can be easily harvested by spambots, defeating any visual obfuscation applied to the text.
**Learning:** Hardcoding `mailto:` URLs nullifies text-based obfuscation. Furthermore, directly assigning DOM attribute values to URL properties without `encodeURIComponent()` can trigger CodeQL DOM XSS alerts. Lastly, concatenating variables into `innerHTML` is insecure; safe DOM construction requires `document.createElement()` and `.textContent`.
**Prevention:** Maintain obfuscated text in HTML, then use client-side JS to dynamically construct an accessible native `mailto:` link wrapped in `encodeURIComponent()`. Provide an interactive "Copy to Clipboard" button utilizing safe DOM methods.
