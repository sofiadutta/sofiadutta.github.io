# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.
## 2025-01-08 - Debouncing Scroll Events for Performance
**Learning:** The `$(window).scroll` listener was firing on every tick, performing multiple DOM queries (`$('body')`, `$('.js-colorlib-nav-toggle')`) and class modifications on each tick. This causes severe main thread blocking and layout thrashing (jank) on mobile.
**Action:** Always wrap high-frequency events (like `scroll` or `resize`) in a `debounce` or `requestAnimationFrame` throttle, and cache DOM selectors outside the event handler to minimize redundant queries.
## 2025-01-08 - Expensive DOM Selectors in Animation Loops
**Learning:** In scroll-triggered animations (waypoints), using complex descendent selectors like `$('body .animate-box.item-animate')` inside `setTimeout` loops forces the browser to traverse the entire DOM tree repeatedly.
**Action:** When querying for state-based classes (like `.item-animate`), use the simplest selector possible (e.g., `$('.item-animate')`) or cache collections outside the event handler to prevent expensive DOM queries during scrolling.
