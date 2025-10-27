from playwright.sync_api import expect, Page
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_product_page_elements(chromium_page: Page):
    chromium_page.goto('https://www.vseinstrumenti.ru/')

    search_input = chromium_page.locator("[data-qa='header-search-input']")
    search_input.fill('газонокосилка Makita')

    search_button = chromium_page.locator("[data-qa='header-search-button']")
    search_button.click()

    product_name_link = chromium_page.locator("[data-qa='product-name']").first
    product_name_link.click()

    product_title = chromium_page.locator("[data-qa='get-product-title']")
    product_title.is_visible()

    price = chromium_page.locator("[data-qa='price-now']")
    price.is_visible()

    add_to_cart_button = chromium_page.locator("[data-qa='add-to-cart-btn']")
    add_to_cart_button.is_enabled()
    add_to_cart_button.is_visible()
    expect(add_to_cart_button).to_have_text('В корзину')