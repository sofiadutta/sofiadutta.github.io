# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Optimized Scroll Event with requestAnimationFrame
**Learning:** In synchronous scroll event listeners like `$(window).scroll()`, manipulating the DOM (e.g., toggling classes on every scroll tick) can cause rapid layout thrashing and main-thread blocking, significantly degrading scrolling performance and causing jank on mobile devices.
**Action:** When handling scroll events (or resize events that manipulate the DOM heavily), always wrap the handler logic in `window.requestAnimationFrame()` coupled with a boolean `ticking` flag. This ensures the callback only fires once per display refresh, decoupling the event firing rate from the browser's render cycle.
