# Bolt's Journal - Critical Learnings

## 2025-01-08 - Large Asset Bottleneck
**Learning:** `images/about.jpg` is 2.9MB, which is extremely large for a sidebar image. This significantly impacts bandwidth availability for other critical assets (like LCP).
**Action:** Since the environment lacks image processing tools (Pillow, ImageMagick), I cannot resize it programmatically. Future optimizations should prioritize setting up an image optimization pipeline or manually resizing this asset if tools become available.

## 2025-01-08 - LCP Optimization for Background Images
**Learning:** Background images defined in CSS (or inline styles) are often discovered late by the browser. Preloading them via `<link rel="preload">` significantly aids LCP.
**Action:** Always check for critical background images in Hero sections and add preloads for them, especially when image optimization tools are unavailable to reduce their size.
## 2025-01-08 - Package Manager Missing Configuration
**Learning:** Running generic `pnpm lint`, `pnpm test`, or `pnpm run build:scripts` in this environment failed because `package.json` relies on a legacy missing `src` directory structure (`/app/src/js/`) and does not actually have lint or test scripts configured.
**Action:** Do not attempt to run standard Node.js generic scripts (like `pnpm lint` or `pnpm test`) here as they are misconfigured or absent. Rely solely on custom `verify_*.py` tracked Python scripts for regression testing.
