from playwright.sync_api import expect, Page
import pytest

@pytest.mark.smoke
@pytest.mark.search
def test_search_for_item(chromium_page: Page):
    chromium_page.goto('https://www.vseinstrumenti.ru/')

    search_input = chromium_page.locator("[data-qa='header-search-input']")
    search_input.fill('газонокосилка Makita')

    search_button = chromium_page.locator("[data-qa='header-search-button']")
    search_button.click()

    chromium_page.wait_for_timeout(5000)