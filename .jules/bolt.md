# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.
## 2024-11-20 - Debouncing High-Frequency Events in Legacy jQuery
**Learning:** When optimizing legacy jQuery templates, functions like `debounce` might be defined locally within an IIFE (Immediately Invoked Function Expression) rather than being globally available. Automated code reviews might flag these as `ReferenceError`s because they don't perform deep static analysis of the entire IIFE scope.
**Action:** Always verify the local scope definition of utility functions before accepting automated code review rejections that claim a function is undefined. Use `message_user` to explain why the code is correct if the review is a false positive.
