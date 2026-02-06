## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2026-02-06 - Robust Clipboard Copy Fallback
**Vulnerability:** Relying solely on `navigator.clipboard.writeText` causes features to fail silently in insecure contexts (like `file://` or non-HTTPS environments) where the API is restricted or rejects the promise.
**Learning:** `navigator.clipboard` availability and behavior varies wildly across environments. A `catch` block on `writeText` is insufficient if it doesn't explicitly trigger a fallback.
**Prevention:** Always implement a robust fallback using `document.execCommand('copy')` (via a hidden textarea) and ensure it is triggered both when `navigator.clipboard` is missing AND when `writeText` fails/rejects.
