## 2026-02-17 - Bootstrap Version Mismatch
**Learning:** `package.json` dependencies can be misleading in legacy projects. This repo lists Bootstrap 5 but serves Bootstrap 3.3.5 css. Relying on modern utility classes (like `ms-2`) based on `package.json` led to incorrect assumptions.
**Action:** Always verify the actual CSS file content (`head` links) before applying version-specific utility classes. When in doubt or constraints prevent custom CSS, use inline styles for micro-adjustments.
