# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Synchronous Scroll Event Handlers
**Learning:** The legacy codebase frequently binds synchronous operations directly to `$(window).scroll()`, leading to main thread blocking and janky scrolling experiences, especially on less powerful devices. This is a common anti-pattern in older jQuery code.
**Action:** When encountering synchronous `scroll` (or `resize`) event handlers, prioritize refactoring them to use a `requestAnimationFrame`-backed 'ticking' approach. This ensures the handler logic only executes once per frame, preventing performance degradation.
