
## 2025-01-08 - Throttling Scroll Events
**Learning:** High-frequency events like `$(window).scroll` block the main thread if unoptimized, degrading rendering performance. Debouncing delays feedback, causing a disjointed UX.
**Action:** Always use `window.requestAnimationFrame` with a ticking flag for scroll-based UI updates to ensure the callback fires exactly once per frame.
