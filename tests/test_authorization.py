from playwright.sync_api import expect, Page
import pytest

def test_authorization(chromium_page: Page):
    chromium_page.goto('https://www.vseinstrumenti.ru/', wait_until='networkidle')

    login_button = chromium_page.locator("[data-qa='login-and-registration']")
    login_button.click()

    email_input = chromium_page.locator("[data-qa='login']")
    email_input.fill('ttlscrt22@gmail.com')

    email_submit_button = chromium_page.locator("[data-qa='submit']")
    email_submit_button.click()

    password_input = chromium_page.locator("[data-qa='password']")
    password_input.fill('pa$$w0rd')

    password_submit_button = chromium_page.locator("[data-qa='submit']")
    password_submit_button.click()