import pytest
import allure
from playwright.sync_api import Page, Playwright
from _pytest.fixtures import SubRequest

@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(source=f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    allure.attach.file(source=page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

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
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json', record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(source=f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    allure.attach.file(source=page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)