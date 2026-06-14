## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.

## 2024-06-14 - Add Sandbox Attributes to Iframes
**Vulnerability:** Missing `sandbox` attribute on YouTube embeds.
**Learning:** Iframes embedding external content (like YouTube videos) without the `sandbox` attribute present a security risk, as they allow the embedded content to execute scripts, navigate the top-level window, or submit forms by default. This application embedded YouTube videos directly without these constraints.
**Prevention:** Always add the `sandbox` attribute to `<iframe>` tags embedding external or untrusted content. For standard video players like YouTube, restricting capabilities to the bare minimum (e.g., `sandbox="allow-scripts allow-same-origin allow-presentation allow-popups allow-popups-to-escape-sandbox"`) prevents the embedded content from unexpectedly taking over the user's session or performing malicious actions while still allowing normal interactive features.
