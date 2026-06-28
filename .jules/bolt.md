# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.
## 2025-01-08 - Fast-Firing Scroll Events
**Learning:** `$(window).scroll` fires rapidly and continuously during page scrolling. Attaching DOM manipulation (like `hasClass`, `removeClass`) directly to this event blocks the main thread and causes severe layout thrashing/jank on mobile devices.
**Action:** Always wrap fast-firing UI event handlers (scroll, resize, mousemove) that cause visual changes or check classes in a `debounce` function with a low wait time (e.g., 10ms) and immediate execution (`true`) to prevent main thread blocking while keeping the UI responsive.
