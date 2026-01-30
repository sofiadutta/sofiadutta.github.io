import re
import time
from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 720})

        page.goto("http://localhost:8000/index.html")

        # Force animations to complete/show
        page.evaluate("document.querySelectorAll('.animate-box').forEach(el => el.style.opacity = '1')")

        # Scroll to contact section
        contact_section = page.locator("[data-section='contact']")
        contact_section.scroll_into_view_if_needed()

        btn = page.locator("#btn-copy-email")
        expect(btn).to_be_visible()
        expect(btn).to_contain_text("Copy")

        # Screenshot before click
        page.screenshot(path="verification_screenshots/before_click.png")

        btn.click()
        expect(btn).to_contain_text("Copied!", ignore_case=True)
        expect(btn).not_to_have_class(re.compile(r"btn-outline"))

        # Screenshot after click
        page.screenshot(path="verification_screenshots/after_click.png")

        print("Click feedback verified. Waiting for revert...")
        time.sleep(2.5) # Wait for 2s timeout + buffer

        expect(btn).to_contain_text("Copy", ignore_case=True)
        expect(btn).to_have_class(re.compile(r"btn-outline"))

        # Screenshot after revert
        page.screenshot(path="verification_screenshots/after_revert.png")

        print("Verification passed: Button reverted to original state.")

        browser.close()

if __name__ == "__main__":
    run()
