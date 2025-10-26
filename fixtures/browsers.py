import pytest
from playwright.sync_api import Page, Playwright

@pytest.fixture
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.vseinstrumenti.ru/')

    email_input = page.get_by_test_id('')

    password_input = page.get_by_test_id('')

    login_button = page.get_by_test_id('')

    context.storage_state(path='browser-state.json')