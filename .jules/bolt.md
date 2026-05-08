# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Unthrottled jQuery Scroll Listener Anti-Pattern
**Learning:** The codebase relies on unthrottled jQuery `$(window).scroll()` event handlers combined with `$('body').hasClass()` checks. This causes severe main thread blocking and layout thrashing as a new jQuery object is continuously instantiated and evaluated during high-frequency scroll events.
**Action:** Always replace unthrottled jQuery scroll listeners with native `window.addEventListener('scroll', ...)`, use `{ passive: true }` to unblock scrolling, replace jQuery DOM queries with native equivalents like `document.body.classList.contains()`, and throttle DOM updates with `requestAnimationFrame` and a boolean lock.
