## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2025-02-19 - Added Sandbox to YouTube iFrames
**Vulnerability:** YouTube `iframe` embeds were missing the `sandbox` attribute, potentially allowing the embedded content broad capabilities within the top-level browsing context.
**Learning:** Adding the `sandbox` attribute to external embeds is an excellent defense-in-depth security practice. However, when sandboxing standard third-party media players like YouTube, standard flags like `allow-scripts`, `allow-same-origin`, and `allow-presentation` are required for core functionality.
**Prevention:** When sandboxing YouTube embeds, ensure you also include `allow-popups` and `allow-popups-to-escape-sandbox` to prevent functional regressions like the inability to open external YouTube links in a new tab.
