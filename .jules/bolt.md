# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-27 - Phantom Dependencies & Resource Contention
**Learning:** Found `fonts/flaticon/font/flaticon.css` linked in `index.html` but the file/directory did not exist (404). Also, `images/about.jpg` (2.9MB) was being preloaded despite not being the LCP candidate, causing bandwidth contention.
**Action:** Remove 404 links (after verifying usage) and remove preloads for large, non-critical assets to prioritize LCP.
