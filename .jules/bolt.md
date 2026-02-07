# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - CSP Compliance vs Performance
**Learning:** `Content-Security-Policy: script-src 'self'` blocks inline scripts, which are usually the fastest way to implement tiny optimizations (like class toggling) without a network request.
**Action:** When CSP is strict, use a tiny external script (e.g., `js/init.js`) instead of an inline script. While it incurs a network request, it respects security boundaries. Ensure the file is small (< 1KB) to minimize latency.
