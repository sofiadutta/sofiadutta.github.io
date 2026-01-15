# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.

## 2025-01-08 - Persistent Event Listeners & CSP
**Learning:** The mobile menu implementation attached a permanent `scroll` listener to `window` to close the menu on scroll. This ran on every frame of scrolling even when the menu was closed. Also, Playwright's `wait_for_function` fails on pages with strict CSP (`unsafe-eval` blocked), requiring the use of selectors or other wait strategies.
**Action:** When auditing legacy jQuery/JS, check for global event listeners attached in initialization that check state; refactor them to be dynamically attached/detached. For verification, avoid `wait_for_function` with string arguments if CSP is strict.
