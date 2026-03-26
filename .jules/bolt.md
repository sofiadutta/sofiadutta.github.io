# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Main Thread Blocking on Mobile Menu Scroll
**Learning:** The offcanvas mobile menu used a raw, unthrottled `$(window).scroll` event listener to close the menu. This fired synchronously hundreds of times during a single scroll, blocking the main thread and causing noticeable jank on mobile devices.
**Action:** Replaced with a `window.requestAnimationFrame` loop and a boolean `ticking` flag. This ensures the scroll handler only executes once per display frame (max 60fps), drastically reducing JS execution time without sacrificing visual responsiveness.
