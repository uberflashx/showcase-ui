import pytest
from playwright.sync_api import Page, Playwright
from _pytest.fixtures import SubRequest
from tools.playwright.pages import initialize_playwright_page
from config import settings


@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param
    )

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    page.goto('https://www.vseinstrumenti.ru')

    login_button = page.locator("[data-qa='login-and-registration']")
    login_button.click()

    email_input = page.locator("[data-qa='login']")
    email_input.fill(settings.test_user.email)

    email_submit_button = page.locator("[data-qa='submit']")
    email_submit_button.click()

    password_input = page.locator("[data-qa='password']")
    password_input.fill(settings.test_user.password)

    password_submit_button = page.locator("[data-qa='submit']")
    password_submit_button.click()

    context.storage_state(path=settings.browser_state_file)

    browser.close()

@pytest.fixture(params=settings.browsers)
def page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=settings.browser_state_file
    )