import pytest
from playwright.sync_api import Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.vseinstrumenti.ru/')

    login_button = page.locator("[data-qa='login-and-registration']")
    login_button.click()

    email_input = page.locator("[data-qa='login']")
    email_input.fill('ttlscrt22@gmail.com')

    email_submit_button = page.locator("[data-qa='submit']")
    email_submit_button.click()

    password_input = page.locator("[data-qa='password']")
    password_input.fill('pa$$w0rd')

    password_submit_button = page.locator("[data-qa='submit']")
    password_submit_button.click()

    context.storage_state(path='browser-state.json')

    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    return page