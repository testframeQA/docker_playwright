from playwright.sync_api import Page

test_url = "https://brgoldsmith.com"

def test_load_site(browser_name, device_type, playwright):
    browser = playwright[browser_name].launch()
    if device_type == "mobile":
        context = browser.new_context(
            viewport={"width": 375, "height": 667},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
        )
    else:
        context = browser.new_context()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()
    response = page.goto(test_url)
    
    # Confirm pageload successful
    assert response.status == 200

    # Take a screenshot
    page.screenshot(path=f"screenshots/{browser_name}_{device_type}_screenshot.png")

    # Stop tracing
    context.tracing.stop(path=f"traces/{browser_name}_{device_type}_trace.zip")

    context.close()
    browser.close()
