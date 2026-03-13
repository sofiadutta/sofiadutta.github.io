import os
from playwright.sync_api import sync_playwright

def verify_scroll(page):
    # Navigate to local file
    file_url = f"file://{os.getcwd()}/index.html"
    page.goto(file_url)

    # Trigger offcanvas menu
    page.evaluate('document.querySelector(".js-colorlib-nav-toggle").click()')
    page.wait_for_timeout(500)

    # Take screenshot of open menu
    page.screenshot(path="verification_screenshots/menu_open.png")

    # Scroll page
    page.evaluate('window.scrollBy(0, 100)')
    page.wait_for_timeout(500)

    # Take screenshot after scroll
    page.screenshot(path="verification_screenshots/menu_closed_after_scroll.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use mobile viewport to trigger offcanvas behavior
        context = browser.new_context(viewport={'width': 400, 'height': 800})
        page = context.new_page()
        try:
            verify_scroll(page)
        finally:
            browser.close()