1. **Refactor jQuery scroll listener to native passive event listener in `js/main.js`**
   - Replace `$(window).scroll(...)` with `window.addEventListener('scroll', ..., { passive: true })` inside the `mobileMenuOutsideClick` function.
   - Use `document.querySelectorAll('.js-colorlib-nav-toggle').forEach(...)` to ensure matching jQuery's behavior.
   - Use `document.body.classList` to toggle `offcanvas` class.
2. **Verify changes visually and run tests**
   - Use a Playwright script to verify the mobile menu toggle and scroll behavior.
   - Ensure the scroll event successfully removes the `offcanvas` class without regressions.
3. **Complete pre-commit steps**
   - Run necessary checks or verification required before committing.
4. **Submit PR**
   - Create a PR with formatted title and description following Bolt's specific structure.
