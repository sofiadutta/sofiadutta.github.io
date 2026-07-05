# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Inconsistent Event Debouncing
**Learning:** The codebase includes a `debounce` utility that is used for `resize` events, but high-frequency `scroll` events that trigger immediate visual UI changes (like closing the offcanvas menu) were left unoptimized, causing potential main-thread blocking.
**Action:** Always verify if global event listeners are properly debounced. When optimizing listeners tied to immediate UI changes, configure the debounce utility to execute immediately on the leading edge (e.g., `immediate = true`) to prevent UX lag.
