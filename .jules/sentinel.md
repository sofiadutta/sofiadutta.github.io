## 2024-05-22 - Legacy JS Blocking Security Fixes
**Vulnerability:** Hidden runtime errors in legacy JavaScript (`$(...).stick_in_parent is not a function`).
**Learning:** Security refactoring (moving inline scripts to external files) can expose pre-existing dormant bugs. In this case, a missing jQuery plugin caused the entire `main.js` to crash, making it look like the security fix failed.
**Prevention:** When refactoring legacy frontend code, wrap plugin calls in existence checks (e.g., `if ($.fn.plugin)`) and verify the baseline console state before starting work.

## 2025-02-19 - CSP Violation Fix for Inline Script
**Vulnerability:** Inline `document.write` script in `index.html` was blocked by the existing Content Security Policy (CSP) which correctly restricts `script-src` to `self` and specific domains, without allowing `unsafe-inline`.
**Learning:** Even "harmless" inline scripts like printing the current year are security violations under strict CSPs. The existing code was actually broken (script blocked) because of the security policy.
**Prevention:** Avoid inline JavaScript entirely. Move all logic to external `.js` files or use DOM manipulation from existing scripts.
## 2024-05-18 - Client-side Email De-obfuscation
**Vulnerability:** Cleartext email addresses were exposed in the HTML source code, making them vulnerable to automated scraping by spam bots. Previous attempts to obfuscate the email address broke native browser link functionality and accessibility.
**Learning:** Hardcoding cleartext email addresses defeats anti-spam measures. When implementing obfuscation, dynamically generating `mailto:` links with JavaScript can lead to DOM XSS vulnerabilities if the text is not properly encoded before assignment to the `href` attribute. Furthermore, replacing native links with JavaScript click handlers breaks middle-click, hover previews, and screen readers.
**Prevention:** Maintain obfuscated text in the static HTML source. Use client-side JavaScript to read the obfuscated text, decode it securely, construct native `mailto:` links (using `encodeURIComponent()` for the `href` attribute to prevent DOM XSS), and dynamically inject them along with supplementary features like a "Copy to Clipboard" button. This ensures both security against spam bots and a robust, accessible user experience.
