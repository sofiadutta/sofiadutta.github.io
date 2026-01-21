# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-21 - Global Event Listener Overhead
**Learning:** The template used global `scroll` and `click` listeners that fired on every interaction to check for a specific class (`offcanvas`). This is inefficient, especially for scroll events.
**Action:** Refactor such listeners to be dynamically attached/detached only when the relevant state (e.g., menu open) is active. This creates a "Zero Cost" state when the feature is idle.

## 2025-01-21 - Preload Contention
**Learning:** Preloading non-critical assets (like `images/about.jpg` which is hidden on mobile) competes with LCP assets (`images/img_bg_2.jpg`). Removing the preload for the non-critical asset saves bandwidth (~3MB) without degrading the critical path.
**Action:** Audit `<link rel="preload">` tags to ensure they are reserved only for critical, above-the-fold assets.
