# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Conditional Preloading for Large Sidebar Image
**Learning:** `images/about.jpg` (2.9MB) was being preloaded unconditionally, wasting bandwidth on mobile where the sidebar is hidden.
**Action:** Added `media="(min-width: 769px)"` to the `<link rel="preload">` tag. This ensures the asset is only preloaded on devices where it is likely to be visible (desktop), significantly improving initial load performance on mobile.
