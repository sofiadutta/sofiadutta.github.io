# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2026-03-21 - Unthrottled Scroll Event DOM Queries
**Learning:** The window scroll event at line 152 performs uncached jQuery lookups for body and nav toggle elements on every tick, causing excessive layout thrashing and blocking the main thread during scrolling.
**Action:** When handling high-frequency events like scrolling, always cache DOM queries and throttle execution using requestAnimationFrame to decouple logic from the event loop.
