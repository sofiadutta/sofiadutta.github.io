# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - UX Considerations with Scroll Debouncing
**Learning:** While `debounce` is useful for saving CPU cycles, applying it to immediate visual updates (like closing a menu on scroll) causes a noticeable delay and poor UX because it waits for the scroll to *stop* before firing.
**Action:** For continuous events tied to immediate visual feedback, use `window.requestAnimationFrame` with a throttling boolean flag (e.g., `ticking = false;`) instead of a traditional debounce. This ensures the update happens smoothly within the browser's render cycle without blocking the main thread.
