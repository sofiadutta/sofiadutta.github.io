## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2025-02-23 - Missing iframe Sandbox Directives
**Vulnerability:** Third-party embedded content via `iframe` elements (e.g., YouTube videos) lacked the `sandbox` attribute, leaving them with full permissions in the context of the embedding site.
**Learning:** While embedding content from trusted sources like YouTube is common, failing to restrict the `iframe` creates a potential vulnerability if the embedded source is compromised, allowing for top-level navigation, automatic downloads, or potential cross-site scripting (XSS) breakouts.
**Prevention:** Always apply the `sandbox` attribute to third-party `iframe` embeds with the least privilege necessary for the content to function (e.g., `sandbox="allow-scripts allow-same-origin allow-presentation allow-popups"` for standard video embeds).
