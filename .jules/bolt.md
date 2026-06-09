# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.
## 2025-01-09 - Scroll Event Listener Bottleneck
**Learning:** Scroll events fire rapidly, and non-passive listeners block the browser's main thread from rendering scroll updates while waiting to see if `preventDefault()` will be called. In jQuery, `$(window).scroll()` attaches a non-passive listener by default.
**Action:** When refactoring scroll event listeners (e.g., from jQuery to native DOM APIs) for performance optimizations, always use `window.addEventListener('scroll', ..., { passive: true })` to prevent scroll jank and layout thrashing.
