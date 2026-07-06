# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Scroll Event Optimization
**Learning:** Adding debouncing to global scroll listeners is essential. Without it, the browser fires scroll events almost constantly (dozens per frame), which causes significant main-thread blocking when querying or modifying the DOM. Using a debouncer with the `immediate` flag set to `true` on UI actions like offcanvas menu closing ensures that the visual feedback is instant on the leading edge without lagging, while still saving CPU cycles.
**Action:** Always wrap global scroll and resize event listeners in `debounce(func, wait, immediate)` in frontend work, ensuring `immediate = true` if visual layout adjustments need to appear perfectly synchronized without lag.
