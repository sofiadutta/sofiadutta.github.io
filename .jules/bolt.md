# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-09 - Scroll Event Listener Bottleneck
**Learning:** In this codebase, the global window scroll listener used to dismiss the offcanvas menu fires synchronously on every pixel scrolled, causing main thread blocking. However, standard trailing debouncing introduces unacceptable UI lag for interactions that require immediate feedback.
**Action:** Always configure the `debounce` utility to execute immediately on the leading edge (`immediate: true`) when optimizing event listeners that trigger immediate visual UI changes (like offcanvas menus).
