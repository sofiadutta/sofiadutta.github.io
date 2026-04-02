from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"file://{os.getcwd()}/index.html")

    # Let page load
    page.wait_for_timeout(2000)

    # Scroll to bottom
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000)

    # remove animate-box classes
    page.evaluate("document.querySelectorAll('.animate-box').forEach(el => { el.classList.remove('animate-box'); el.style.opacity = '1'; })")

    page.screenshot(path="contact_section.png", full_page=True)
    browser.close()
