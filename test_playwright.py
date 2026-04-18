import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(permissions=['clipboard-read', 'clipboard-write'])
        page = await context.new_page()
        file_url = f"file://{os.getcwd()}/index.html"
        await page.goto(file_url)

        # Let's write the JS to js/main.js
        with open('js/main.js', 'a') as f:
            f.write("""
    // Copy email to clipboard
    var setupEmailCopy = function() {
        var copyBtn = document.getElementById('copy-email-btn');
        var emailSpan = document.getElementById('contact-email');
        if (copyBtn && emailSpan) {
            copyBtn.addEventListener('click', function() {
                var obfuscated = emailSpan.textContent || emailSpan.innerText;
                var email = obfuscated.replace(/\\s/g, '').replace(/DOT/g, '.').replace(/AT/g, '@');

                if (navigator.clipboard && window.isSecureContext) {
                    navigator.clipboard.writeText(email).then(function() {
                        var originalHtml = copyBtn.innerHTML;
                        copyBtn.innerHTML = '<i class="icon-check" aria-hidden="true"></i> Copied!';
                        setTimeout(function() {
                            copyBtn.innerHTML = originalHtml;
                        }, 2000);
                    });
                } else {
                    // Fallback
                    var textArea = document.createElement("textarea");
                    textArea.value = email;
                    textArea.style.position = "fixed";  // avoid scrolling to bottom
                    document.body.appendChild(textArea);
                    textArea.focus();
                    textArea.select();
                    try {
                        document.execCommand('copy');
                        var originalHtml = copyBtn.innerHTML;
                        copyBtn.innerHTML = '<i class="icon-check" aria-hidden="true"></i> Copied!';
                        setTimeout(function() {
                            copyBtn.innerHTML = originalHtml;
                        }, 2000);
                    } catch (err) {
                        console.error('Fallback: Oops, unable to copy', err);
                    }
                    document.body.removeChild(textArea);
                }
            });
        }
    };
    $(function(){
        setupEmailCopy();
    });
            """)

        await page.reload()

        # Test copy button
        await page.locator('#copy-email-btn').click()

        # Check if text changes
        text = await page.locator('#copy-email-btn').inner_text()
        print(f"Button text after click: {text}")

        # Check clipboard content via fallback/secure context logic
        # Actually in playwright file:// is not secure context by default?

        await browser.close()

asyncio.run(main())
