## 2025-02-12 - Handling Clipboard Permissions in Playwright

**Learning:** Playwright in headless mode often denies clipboard write permissions (`navigator.clipboard.writeText`) due to security restrictions or insecure contexts (http://localhost), causing tests to fail even if the logic is correct.

**Action:** Always implement a fallback mechanism (e.g., `document.execCommand('copy')` with a temporary textarea) in the application code to handle permission failures gracefully. This ensures robust functionality across different browser environments and test runners. In Playwright tests, verify the fallback path if the primary clipboard API is expected to fail.
