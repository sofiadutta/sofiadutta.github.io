# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2026-03-16 - Unthrottled Scroll Event Anti-Pattern
**Learning:** The legacy codebase uses unthrottled `$(window).scroll` events to query and update the DOM. This causes layout thrashing and scroll jank, especially on mobile devices.
**Action:** Always throttle high-frequency events (like `scroll`) using `window.requestAnimationFrame` coupled with a ticking boolean flag to decouple the event trigger from the DOM mutation phase.
