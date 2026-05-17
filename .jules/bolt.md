# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Unthrottled jQuery Scroll Listeners
**Learning:** The codebase relies on unthrottled jQuery scroll event listeners (e.g., `$(window).scroll`) combined with continuous jQuery DOM queries (e.g., `$('body').hasClass`). This causes layout thrashing, continuous garbage collection, and blocks the main thread during scrolling.
**Action:** Always replace these with native `window.addEventListener('scroll')` using `{ passive: true }`, throttle execution using `requestAnimationFrame` with a boolean lock, and use native DOM APIs (`document.body.classList`) to avoid jQuery object instantiation overhead.
