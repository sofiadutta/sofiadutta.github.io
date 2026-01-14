# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2026-01-14 - Modernizr & CSP
**Learning:** `Modernizr` (16KB) was used solely to switch `no-js` to `js` on `<html>`. Replacing it with a vanilla one-liner saves bandwidth. However, strict CSP forbids inline scripts, forcing even simple logic into external files (`js/init.js`).
**Action:** When replacing library bloat with simple scripts, always verify CSP headers first to decide between inline vs. external script placement.
