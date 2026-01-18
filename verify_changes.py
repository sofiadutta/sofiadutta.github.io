from playwright.sync_api import sync_playwright

def verify(page):
    print("Navigating to file:///app/index.html")
    page.goto("file:///app/index.html")

    # Check Copyright
    footer = page.locator(".colorlib-footer")
    copyright_text = footer.inner_text()
    print(f"Footer text: {copyright_text}")

    # Verify no double copyright
    if "©Copyright ©" in copyright_text:
        print("FAIL: Double copyright found")
    elif "Copyright ©" in copyright_text:
        print("PASS: Copyright text looks correct")
    else:
        print("FAIL: Copyright text unexpected")

    # Check Social Links
    linkedin = page.locator("a[aria-label='LinkedIn Profile']")
    title = linkedin.get_attribute("title")
    print(f"LinkedIn title: {title}")

    if title == "LinkedIn Profile":
        print("PASS: LinkedIn title correct")
    else:
        print("FAIL: LinkedIn title incorrect")

    icon = linkedin.locator("i")
    aria_hidden = icon.get_attribute("aria-hidden")
    print(f"Icon aria-hidden: {aria_hidden}")

    if aria_hidden == "true":
        print("PASS: Icon aria-hidden correct")
    else:
        print("FAIL: Icon aria-hidden incorrect")

    # Check decorative icons in Timeline
    timeline_icon = page.locator(".timeline-icon").first.locator("i")
    aria_hidden_timeline = timeline_icon.get_attribute("aria-hidden")
    print(f"Timeline icon aria-hidden: {aria_hidden_timeline}")

    if aria_hidden_timeline == "true":
        print("PASS: Timeline icon aria-hidden correct")
    else:
        print("FAIL: Timeline icon aria-hidden incorrect")

    # Check decorative icons in Services (About)
    services_icon = page.locator(".services .icon2 i").first
    aria_hidden_services = services_icon.get_attribute("aria-hidden")
    print(f"Services icon aria-hidden: {aria_hidden_services}")

    if aria_hidden_services == "true":
        print("PASS: Services icon aria-hidden correct")
    else:
        print("FAIL: Services icon aria-hidden incorrect")

    # Take screenshot of footer
    # Use JS scroll because scroll_into_view_if_needed can be flaky in some envs
    page.evaluate("document.querySelector('.colorlib-footer').scrollIntoView()")
    page.screenshot(path="/app/verification_footer.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
