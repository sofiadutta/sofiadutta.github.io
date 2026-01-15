from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    # Use a mobile viewport
    page = browser.new_page(viewport={"width": 375, "height": 667})

    print("Loading page...")
    page.goto("file:///app/index.html")

    # Check initial state
    body = page.locator("body")
    assert "offcanvas" not in (body.get_attribute("class") or "")

    # Click burger menu
    print("Clicking burger menu...")
    toggle = page.locator(".js-colorlib-nav-toggle")
    toggle.click()

    # Wait for offcanvas class
    print("Waiting for offcanvas class...")
    page.wait_for_selector("body.offcanvas", state="attached", timeout=5000)
    print("Menu opened, offcanvas class present.")

    page.screenshot(path="menu_open.png")

    # Scroll
    print("Scrolling...")
    # Using function instead of string to avoid CSP issues if possible, though string usually works for evaluate
    page.evaluate("() => window.scrollBy(0, 100)")

    # Wait for offcanvas class to disappear
    print("Waiting for menu to close...")
    try:
        # Use selector which is CSP safe
        page.wait_for_selector("body:not(.offcanvas)", state="attached", timeout=5000)
        print("Menu closed after scroll.")
    except Exception as e:
        print("Menu DID NOT close after scroll.")
        print(f"Body class: {body.get_attribute('class')}")
        raise e

    page.screenshot(path="menu_closed.png")

    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
