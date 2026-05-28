# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2024-05-28 - jQuery Scroll Event Listeners Block Rendering
**Learning:** The legacy codebase uses `$(window).scroll()` which attaches non-passive event listeners, blocking the main thread during scrolling and causing scroll jank.
**Action:** When refactoring scroll event listeners for performance optimizations, always use `window.addEventListener('scroll', ..., { passive: true })` to prevent the browser from blocking scroll rendering while waiting for a potential `preventDefault()`. Use native DOM APIs (e.g., `document.querySelectorAll().forEach()`) instead of jQuery for operations inside the scroll listener to minimize overhead.
