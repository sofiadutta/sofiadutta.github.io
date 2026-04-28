# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2026-04-28 - Unthrottled jQuery Scroll Listeners
**Learning:** Frequent events like `scroll` attached via jQuery (`$(window).scroll(...)`) can cause significant main thread blocking, especially when instantiating new jQuery objects inside the callback (e.g., `$('body')`).
**Action:** Always use native `window.addEventListener('scroll', ...)` with `{ passive: true }`, throttle DOM checks via `requestAnimationFrame` with a boolean lock, and use native DOM APIs (`document.body.classList.contains`) to avoid continuous jQuery garbage collection overhead.
