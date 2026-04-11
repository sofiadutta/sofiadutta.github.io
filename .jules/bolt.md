# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Throttling Scroll Event Listeners
**Learning:** Unthrottled jQuery scroll event listeners (e.g., `$(window).scroll(...)`) trigger multiple times per pixel scrolled, leading to layout thrashing and main thread blocking, especially when repeatedly checking DOM state and classes.
**Action:** Replace unthrottled jQuery scroll listeners with native `window.addEventListener('scroll', ...)` and throttle DOM queries and updates using `window.requestAnimationFrame` along with a boolean lock variable. This defers the work until the browser is ready to repaint, significantly improving scroll performance.
