## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2025-03-08 - Iframe Sandbox Security Enhancement
**Vulnerability:** YouTube iframes embedded without the `sandbox` attribute. This is a potential risk because an iframe without restrictions can execute harmful scripts, attempt top-level navigation, or otherwise interfere with the hosting application if the embedded content is compromised or acts maliciously.
**Learning:** Third-party content embedded via `iframe` elements should always follow defense-in-depth principles. Even for trusted sources like YouTube, applying a `sandbox` attribute restricts the embedded page to only the required capabilities, mitigating potential XSS or unauthorized navigation breakouts.
**Prevention:** Whenever embedding third-party content using an `iframe`, always apply a restrictive `sandbox` attribute (e.g., `sandbox="allow-scripts allow-same-origin allow-presentation allow-popups"` for standard media embeds) to explicitly allow necessary features while blocking potentially harmful behaviors.
