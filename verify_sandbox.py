from playwright.sync_api import sync_playwright

def verify(page):
    print("Navigating to file:///app/index.html")
    page.goto("file:///app/index.html")

    print("Checking YouTube iframes for sandbox attribute...")

    # Locate all iframes with src containing youtube.com
    iframes = page.locator("iframe[src*='youtube.com']")
    count = iframes.count()
    print(f"Found {count} YouTube iframes.")

    if count == 0:
        print("FAIL: No YouTube iframes found.")
        exit(1)

    expected_sandbox = "allow-scripts allow-same-origin allow-presentation allow-popups"

    all_pass = True
    for i in range(count):
        frame = iframes.nth(i)
        sandbox = frame.get_attribute("sandbox")
        title = frame.get_attribute("title")
        print(f"Iframe {i+1} ({title}): sandbox='{sandbox}'")

        if sandbox == expected_sandbox:
            print("PASS: Sandbox attribute is correct.")
        else:
            print(f"FAIL: Sandbox attribute mismatch. Expected '{expected_sandbox}', got '{sandbox}'")
            all_pass = False

    if all_pass:
        print("ALL SECURITY CHECKS PASSED")
    else:
        print("SECURITY CHECKS FAILED")
        exit(1)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify(page)
        except Exception as e:
            print(f"Error: {e}")
            exit(1)
        finally:
            browser.close()
