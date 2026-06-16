# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.
## 2025-01-08 - Passive Scroll Listeners
**Learning:** In `js/main.js`, the scroll event listener `$(window).scroll(function(){...})` for closing the mobile menu is blocking the main thread because jQuery binds scroll events without `{ passive: true }` by default. This degrades scroll performance, particularly on mobile devices.
**Action:** Refactor scroll-bound listeners (like the offcanvas mobile menu toggle) to use the native DOM API `window.addEventListener('scroll', handler, { passive: true })` instead of jQuery to prevent scroll rendering blocks.
