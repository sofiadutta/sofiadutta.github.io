# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-02-09 - Conditional Preloading for Sidebar Image
**Learning:** The sidebar image `images/about.jpg` (2.9MB) was being preloaded unconditionally, causing massive bandwidth waste on mobile where the sidebar is hidden by default.
**Action:** Used `media="(min-width: 769px)"` on the `<link rel="preload">` tag to restrict preloading to desktop viewports where the sidebar is visible. This is a high-impact, low-risk optimization for responsive sites with large assets in hidden-by-default components.
