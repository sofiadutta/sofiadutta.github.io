# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - False Positive in Code Review for Local IIFE Scopes
**Learning:** Automated code reviews may incorrectly flag locally defined utility functions (like `debounce` inside an IIFE in `js/main.js`) as `ReferenceError: function is not defined` because they evaluate the patch out of context and assume the function needs to be globally available or imported.
**Action:** When a code review rejects a valid patch due to a false positive about a missing function that is actually defined within the file's local scope, use the `message_user` tool to explicitly explain the local IIFE scope to bypass the incorrect blockage, rather than modifying the code to appease the reviewer.
