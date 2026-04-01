# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Main Thread Blocking Scroll Listeners
**Learning:** The application was using an unthrottled jQuery `$(window).scroll(...)` listener to close the mobile offcanvas menu. Since scroll events fire rapidly during scrolling, triggering jQuery DOM checks (`hasClass`) for every event can lead to layout thrashing and main thread blocking, reducing scrolling performance.
**Action:** Use native DOM APIs (`classList`, `querySelector`) wrapped in `requestAnimationFrame` with a boolean lock to ensure layout queries and DOM updates happen efficiently synced with the browser's render cycle.
