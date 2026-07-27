# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - jQuery Scroll Event Bottlenecks
**Learning:** This codebase relies heavily on jQuery and uses a specific anti-pattern of repeatedly querying the DOM (e.g., `$('body')`) directly inside high-frequency `$(window).scroll()` event listeners. This evaluates selectors on every scroll tick, creating unnecessary CPU overhead and garbage collection pressure.
**Action:** When working in this specific codebase, always check scroll and resize event listeners for inline DOM queries and refactor them to cache selectors outside the callback scope.
