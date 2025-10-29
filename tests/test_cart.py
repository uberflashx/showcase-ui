from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
def test_adding_product_to_cart(chromium_page: Page):
    chromium_page.goto('https://www.vseinstrumenti.ru/', wait_until='networkidle')

    search_input = chromium_page.locator("[data-qa='header-search-input']")
    search_input.fill('газонокосилка Makita')

    search_button = chromium_page.locator("[data-qa='header-search-button']")
    search_button.click()

    add_to_cart_from_tile_button = chromium_page.locator("[data-qa='product-add-to-cart-button']").first
    add_to_cart_from_tile_button.click()

    go_to_basket_button = chromium_page.locator("[data-qa='go-to-basket']")
    go_to_basket_button.click()

    product_item = chromium_page.locator("[data-qa='product-item']")
    expect(product_item).to_be_visible()

    total_price = chromium_page.locator("[data-qa='checkout-total-total-price']")
    expect(total_price).to_be_visible()

    create_order_button = chromium_page.locator("[data-qa='cart-total-order-create-button']")
    expect(create_order_button).to_be_enabled()
    expect(create_order_button).to_be_visible()
    expect(create_order_button).to_have_text('Оформить заказ')