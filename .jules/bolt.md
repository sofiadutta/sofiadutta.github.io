# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2026-03-12 - requestAnimationFrame for scroll handlers
**Learning:** Relying on 'debounce' for scroll handlers can cause UI delay or 'jank', while unthrottled execution blocks the main thread. In jQuery templates where `$(window).scroll` is used for layout toggling, neither approach is ideal for instantaneous UX feedback.
**Action:** Use `window.requestAnimationFrame` coupled with a 'ticking' boolean flag for all continuous event handlers (like scroll or resize) to sync DOM updates with the browser's render cycle, ensuring maximum performance without visual lag.
