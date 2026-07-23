# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-10-24 - Uncached DOM Selectors in Scroll Events
**Learning:** Found an anti-pattern in `js/main.js` where `$('body')` and `$('.js-colorlib-nav-toggle')` were queried directly inside the `window.scroll` event listener, causing unnecessary jQuery object instantiation and DOM querying 60+ times per second during scroll.
**Action:** Cache DOM selectors in variables (e.g., `var $body = $('body');`) outside of high-frequency event listeners to avoid redundant processing overhead.
