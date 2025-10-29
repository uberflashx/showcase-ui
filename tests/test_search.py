from playwright.sync_api import expect, Page
import pytest

@pytest.mark.parametrize('product, brand', [('газонокосилка', 'Makita'), ('кусторез', 'Dewalt')])
@pytest.mark.smoke
@pytest.mark.search
def test_search_for_product(chromium_page: Page, product: str, brand: str):
    chromium_page.goto('https://www.vseinstrumenti.ru/', wait_until='networkidle')

    search_input = chromium_page.locator("[data-qa='header-search-input']")
    search_input.fill(f'{product} {brand}')

    search_button = chromium_page.locator("[data-qa='header-search-button']")
    search_button.click()

    search_results = chromium_page.locator("[data-qa='listing']")
    search_results.is_visible()