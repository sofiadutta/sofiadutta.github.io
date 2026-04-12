# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.
## 2025-01-08 - Scroll Event Throttling
**Learning:** In legacy codebases using older jQuery versions, scroll event listeners (like `$(window).scroll(...)`) are frequently unthrottled. Since they run synchronously on the main thread, any DOM manipulation within these listeners blocks painting and triggers forced synchronous layouts (layout thrashing), creating significant scroll lag, particularly on mobile devices.
**Action:** Always replace unthrottled jQuery scroll listeners with a native `window.addEventListener('scroll')` paired with a `requestAnimationFrame` loop and a boolean lock (`scrollTicking`). This cleanly decouples event firing frequency from DOM updates, ensuring smooth 60fps scrolling. Furthermore, when replacing jQuery selectors (`$('.class')`) inside these loops, use `document.querySelectorAll('.class')` and iterate through the NodeList to safely replicate jQuery's multi-element matching behavior, as `querySelector` only returns the first match and could introduce subtle bugs if multiple elements share the class.
