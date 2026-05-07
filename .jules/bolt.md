# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.
## 2025-01-09 - Scroll Listener Optimization
**Learning:** Legacy templates often use unthrottled jQuery `$(window).scroll(...)` event listeners, which fire continuously during scrolling and repeatedly execute expensive jQuery DOM queries (`$('body').hasClass(...)`). This causes layout thrashing and blocks the main thread, resulting in janky scrolling.
**Action:** When encountering unthrottled scroll listeners, always replace them with native `window.addEventListener('scroll', ...)` using a boolean lock (`ticking`), `requestAnimationFrame` for throttling updates, and the `{ passive: true }` option to allow the browser to perform smooth scrolling without waiting for JavaScript execution. Also, swap jQuery class toggling for native `document.body.classList` APIs to avoid garbage collection overhead from continuous jQuery object instantiation.
