import os
import time
import re
from playwright.sync_api import sync_playwright, expect

def test_email_obfuscation(page):
    # Navigate to the page
    page.goto("http://localhost:8080/index.html")

    # Locate the Hire me button
    # It has text "Hire me" and class "btn-hire"
    hire_btn = page.locator(".btn-hire")

    # Check it is visible
    expect(hire_btn).to_be_visible()

    # Check attributes
    expect(hire_btn).to_have_attribute("href", "#")
    expect(hire_btn).to_have_attribute("data-user", "sofia.dutta17")
    expect(hire_btn).to_have_attribute("data-domain", "gmail.com")
    expect(hire_btn).to_have_class(re.compile(r"js-email-protect"))

    # Verify NO target="_blank"
    target = hire_btn.get_attribute("target")
    assert target != "_blank", f"Expected target != '_blank', got {target}"

    # Scroll to it for screenshot
    hire_btn.scroll_into_view_if_needed()
    # Force wait a bit for animations
    page.wait_for_timeout(1000)

    # Take screenshot
    os.makedirs("/home/jules/verification", exist_ok=True)
    page.screenshot(path="/home/jules/verification/email_fix.png")
    print("Screenshot saved to /home/jules/verification/email_fix.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use desktop viewport
        context = browser.new_context(viewport={"width": 1280, "height": 1024})
        page = context.new_page()
        try:
            test_email_obfuscation(page)
        finally:
            browser.close()
