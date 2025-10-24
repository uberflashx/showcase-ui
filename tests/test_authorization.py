from playwright.sync_api import sync_playwright


def test_authorization():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://www.vseinstrumenti.ru/')

        page.wait_for_timeout(100000)