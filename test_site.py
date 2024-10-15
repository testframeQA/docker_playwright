import pytest
from playwright.sync_api import Page

TEST_URL = "https://www.test.com"

@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
@pytest.mark.parametrize("device_type", ["desktop", "mobile"])
def test_load_site(browser_name, device_type, playwright):
    browser = playwright[browser_name].launch()
    if device_type == "mobile":
            context = browser.new_context(
            trace_dir="trace/",
            viewport={"width": 375, "height": 667},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
        )
    else:
        context = browser.new_context(trace_dir="trace/")

    page = context.new_page()
    response = page.goto(TEST_URL)
    assert response.status == 200
    page.screenshot(path=f"screenshots/{browser_name}_{device_type}_screenshot.png")

    context.close()
    browser.close()
