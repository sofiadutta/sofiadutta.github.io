## 2024-05-23 - [Icon-Only Buttons and "Ghost" Sources]
**Learning:** Found a repository where `package.json` scripts referred to a missing `src` directory, implying the `index.html` at the root was the intended "source of truth" for this simplified version. This is a common pattern in "starter" templates where the advanced build setup is stripped out but configuration files remain.
**Action:** Always verify if build scripts actually correspond to the file structure before relying on them. When `src` is missing in a simple web project, edit the root HTML directly.

## 2024-05-23 - [Accessible Background Images and Skip Links]
**Learning:** Found critical content implemented as background images (profile photo). This pattern is invisible to screen readers unless explicitly marked with `role="img"` and `aria-label`. Also, single-page layouts like this desperately need "Skip to Content" links to allow keyboard users to bypass long navigation menus.
**Action:** When auditing legacy themes, check all `data-bg` or `background-image` inline styles for meaningful content and add ARIA attributes. Always ensure a skip link exists for sidebars.

## 2024-05-23 - [JS Crashing due to Undefined Function Call]
**Learning:** Discovered that a `ReferenceError` (calling undefined `updateYear()`) in the main JS file was silently blocking subsequent script execution, including critical features like lazy loading images. This highlights how fragile single-file script bundles can be.
**Action:** When auditing legacy JS, always check for console errors first. If a function call blocks execution, verify if it's defined. If not, and a correct alternative exists (`updateCopyrightYear`), remove the blocker.

## 2024-05-23 - [Tooltips for Icon-Only Buttons]
**Learning:** Icon-only buttons (like social links) are ambiguous for mouse users. While `aria-label` helps screen readers, sighted users benefit significantly from a native browser tooltip via the `title` attribute.
**Action:** Always add `title` attributes matching the `aria-label` for icon-only interactive elements.
## 2024-05-24 - Obfuscated Email Copy UX
**Learning:** Obfuscating emails for spam protection (e.g. 'sofia DOT dutta AT gmail') creates high user friction when they actually want to contact the person. Reconstructing the valid email dynamically via `data-*` attributes and copying it directly to the clipboard perfectly balances spam mitigation with a seamless user experience.
**Action:** When encountering obfuscated text meant for user utility, implement a one-click action to resolve and execute the primary intent (copying, linking) rather than forcing the user to manually parse and retype the information.
