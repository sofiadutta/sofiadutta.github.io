# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Caching DOM Selectors in High-Frequency Events
**Learning:** Querying the DOM inside high-frequency event listeners (like `scroll` or `resize`) using jQuery creates significant overhead and main thread blocking, as the DOM tree is traversed on every event fire.
**Action:** Always cache jQuery DOM selectors (e.g., `var $body = $('body');`) outside of high-frequency event handlers so the reference is maintained and DOM traversal is bypassed.
