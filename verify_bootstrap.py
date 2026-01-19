from playwright.sync_api import sync_playwright
import os

def verify_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index.html
        page.goto("file:///app/index.html")

        # Wait for the page to load
        page.wait_for_load_state("networkidle")

        # Verify Bootstrap version via console
        bootstrap_version = page.evaluate("$.fn.tooltip.Constructor.VERSION")
        print(f"Bootstrap Version: {bootstrap_version}")

        # Verify jQuery version
        jquery_version = page.evaluate("$.fn.jquery")
        print(f"jQuery Version: {jquery_version}")

        # Verify Hero Section exists and is visible
        hero = page.locator("#colorlib-hero")
        if hero.is_visible():
            print("Hero section is visible.")
        else:
            print("Hero section is NOT visible.")

        # Verify Sidebar
        sidebar = page.locator("#colorlib-aside")
        if sidebar.is_visible():
            print("Sidebar is visible.")

        # Check if sliders are initialized (flexslider)
        # Flexslider adds 'flex-viewport' class
        flex_viewport = page.locator(".flex-viewport")
        if flex_viewport.count() > 0:
            print("FlexSlider seems initialized.")
        else:
            print("FlexSlider NOT found.")

        # Take a screenshot
        os.makedirs("/home/jules/verification", exist_ok=True)
        page.screenshot(path="/home/jules/verification/bootstrap_check.png")

        browser.close()

if __name__ == "__main__":
    verify_site()
