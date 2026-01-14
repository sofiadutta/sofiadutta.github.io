import time
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Set a specific desktop user agent to ensure isMobile.any() returns false
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            viewport={'width': 1200, 'height': 800}
        )
        page = context.new_page()
        page.goto("file:///app/index.html")

        # Wait for scripts to load and fullHeight to run
        page.wait_for_load_state("networkidle")
        time.sleep(1) # Extra buffer for JS execution

        # Get element with .js-fullheight.
        # #colorlib-hero is a good candidate.
        hero = page.locator("#colorlib-hero")

        # Check initial height
        initial_height = hero.evaluate("el => el.style.height")
        print(f"Initial viewport height: 800")
        print(f"Initial element height: {initial_height}")

        if initial_height != "800px":
            print("Warning: Initial height does not match viewport height.")
            # It might be that the script hasn't run or isMobile check failed.
            # Let's check window height in page
            window_height = page.evaluate("window.innerHeight")
            print(f"Window innerHeight: {window_height}")

        # Resize viewport
        print("Resizing viewport to 1200x600...")
        page.set_viewport_size({"width": 1200, "height": 600})

        # Trigger resize event if set_viewport_size doesn't automatically (it should)
        # But for good measure we can wait.
        time.sleep(1) # Wait for debounce (if present) and execution

        # Check new height
        new_height = hero.evaluate("el => el.style.height")
        print(f"New element height: {new_height}")

        if new_height == "600px":
            print("SUCCESS: Element resized to match new viewport height.")
        else:
            print("FAILURE: Element did not resize correctly.")
            print(f"Expected: 600px, Got: {new_height}")

        browser.close()

if __name__ == "__main__":
    run()
