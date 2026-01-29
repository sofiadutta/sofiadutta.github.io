from playwright.sync_api import sync_playwright
import sys

def verify(page):
    print("Navigating to file:///app/index.html")
    page.goto("file:///app/index.html")

    # Locate the "Hire me" button
    # It has class "btn-hire"
    hire_btn = page.locator(".btn-hire")

    if hire_btn.count() == 0:
        print("FAIL: 'Hire me' button not found")
        sys.exit(1)

    print("Found 'Hire me' button")

    # Check attributes
    href = hire_btn.get_attribute("href")
    target = hire_btn.get_attribute("target")
    data_user = hire_btn.get_attribute("data-user")
    data_domain = hire_btn.get_attribute("data-domain")
    class_attr = hire_btn.get_attribute("class")

    print(f"href: {href}")
    print(f"target: {target}")
    print(f"data-user: {data_user}")
    print(f"data-domain: {data_domain}")
    print(f"class: {class_attr}")

    failed = False

    # Check href
    if href and href.startswith("mailto:"):
        print("FAIL: href contains mailto (should be obfuscated)")
        failed = True
    elif href == "#":
        print("PASS: href is '#' as expected")
    else:
        print(f"WARN: href is '{href}' (expected '#')")
        # Not necessarily a fail if it's javascript:void(0) but we planned for #

    # Check target
    if target == "_blank":
        print("FAIL: target is '_blank' (should be removed)")
        failed = True
    else:
        print("PASS: target is not '_blank'")

    # Check data attributes
    if data_user == "sofia.dutta17":
        print("PASS: data-user is correct")
    else:
        print("FAIL: data-user is missing or incorrect")
        failed = True

    if data_domain == "gmail.com":
        print("PASS: data-domain is correct")
    else:
        print("FAIL: data-domain is missing or incorrect")
        failed = True

    # Check class
    if "email-obfuscated" in (class_attr or ""):
        print("PASS: class 'email-obfuscated' is present")
    else:
        print("FAIL: class 'email-obfuscated' is missing")
        failed = True

    if failed:
        sys.exit(1)
    else:
        print("SUCCESS: Email security verification passed")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify(page)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
        finally:
            browser.close()
