# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Passive Event Listeners for Scroll
**Learning:** jQuery's `.scroll()` method binds non-passive event listeners, which forces the browser's main thread to wait and check if `preventDefault()` is called before it can render a scroll frame, causing scroll jank.
**Action:** When refactoring scroll or touch event listeners, always replace jQuery bindings with native DOM APIs using `window.addEventListener('scroll', ..., { passive: true })` to eliminate main-thread blocking and improve scroll performance.
