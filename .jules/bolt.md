# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-02-18 - Conditional Preloading for Large Assets
**Learning:** `rel="preload"` is powerful but can be wasteful if unconditional. Large assets like sidebar images hidden on mobile (~2.9MB) should use the `media` attribute (e.g., `media="(min-width: 769px)"`) to prevent unnecessary downloads on constrained devices while maintaining performance for desktop users.
**Action:** Always audit `preload` tags against the element's visibility across breakpoints. Use `media` queries in `<link>` tags for viewport-dependent assets.
