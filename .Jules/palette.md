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
## 2024-05-23 - [Accessible Copy Buttons for Obfuscated Text]
**Learning:** Obfuscating email addresses (e.g., "name AT domain DOT com") is great for bot protection, but creates friction for users who have to manually decode and copy the text. Implementing a client-side copy button that decodes the text on-the-fly and writes it to the clipboard provides a seamless UX while maintaining the bot protection. Furthermore, using a `<span>` to isolate the text and temporarily disabling the button via `button.disabled = true` prevents rapid clicks from overriding the HTML state.
**Action:** Always wrap obfuscated text in a `<span>` to easily target it, and add an accessible copy button with `aria-label`, `title`, and `aria-live` feedback. Ensure the button is disabled during the active/copied state to prevent HTML override bugs.
