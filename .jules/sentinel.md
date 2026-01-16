## 2025-02-12 - jQuery Upgrade 3.x
**Vulnerability:** jQuery 2.1.4 contained known XSS vulnerabilities (e.g., in `parseHTML`) and lacked modern security fixes.
**Learning:** Upgrading to jQuery 3.x (3.7.1) introduces breaking changes like the removal of `$(window).load()`, `.bind()`, and `.delegate()`. However, static analysis of `js/main.js` and `js/google_map.js` in this specific project showed no usage of these deprecated methods, allowing a clean drop-in replacement without `jquery-migrate`.
**Prevention:** When upgrading legacy libraries, always grep for deprecated method signatures in application code before committing.
