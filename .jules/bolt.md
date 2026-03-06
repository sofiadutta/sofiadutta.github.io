# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Main Thread Blocking on Scroll
**Learning:** `$(window).scroll` is used to hide the mobile offcanvas menu. However, synchronous execution of DOM queries (`hasClass`, `removeClass`) inside scroll handlers can cause layout thrashing and block the main thread, leading to janky scrolling on mobile devices.
**Action:** When implementing scroll event listeners, especially those that trigger layout changes or query the DOM, always throttle the execution using `window.requestAnimationFrame` coupled with a ticking boolean flag. This ensures the callback only runs once per render frame, significantly improving scroll performance and UI responsiveness.
