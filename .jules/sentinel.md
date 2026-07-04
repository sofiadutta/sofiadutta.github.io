## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2025-02-19 - Sandbox Attributes for Third-Party Iframes
**Vulnerability:** YouTube `iframe` embeds in `index.html` were missing `sandbox` attributes, leaving the application open to potential exploits if the embedded content was compromised (e.g., malicious scripts attempting to manipulate the parent page or navigate the top-level window).
**Learning:** While `sandbox` attributes are crucial for security (defense in depth), applying them to complex third-party media players like YouTube requires a careful balance. Restricting too much breaks functionality. Specifically, `allow-popups` and `allow-popups-to-escape-sandbox` are necessary for YouTube iframes to handle authentication and share dialogs correctly without breaking.
**Prevention:** Always add `sandbox` attributes to third-party `iframe` embeds. For standard media players (like YouTube or Vimeo), ensure the attribute includes `allow-scripts allow-same-origin allow-presentation allow-popups allow-popups-to-escape-sandbox` to maintain functionality while preventing dangerous actions like top-level navigation.
