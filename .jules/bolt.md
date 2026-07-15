# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.
## 2025-01-08 - Scroll Event Throttling/Debouncing
**Learning:** `$(window).scroll()` event listener executing jQuery logic to query the DOM `$('body').hasClass('offcanvas')` on every scroll tick blocks the main thread and can cause scroll jank. This is highly problematic, especially on mobile viewports where this logic is relevant.
**Action:** Use the existing local `debounce` wrapper utility on high-frequency window events (like scroll/resize) when executing heavy DOM interactions to increase scroll rendering framerates and minimize main thread utilization.
