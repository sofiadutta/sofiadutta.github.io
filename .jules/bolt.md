# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.
## 2025-01-09 - Scroll Event Debouncing Optimization
**Learning:** Attaching heavy UI state changes (like DOM class manipulation) directly to `$(window).scroll` causes performance lag due to the high frequency of scroll events. Applying a debounce on the leading edge (`immediate = true`) ensures the UI responds instantly to the first scroll tick without processing the hundreds of subsequent ticks in the same gesture.
**Action:** Always wrap scroll and resize event listeners that trigger immediate visual changes with an immediate debounce function to reduce CPU load and layout thrashing.
