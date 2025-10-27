from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
def test_brand_page_elements(chromium_page: Page):
    chromium_page.goto('https://www.vseinstrumenti.ru/')

    search_input = chromium_page.locator("[data-qa='header-search-input']")
    search_input.fill('газонокосилка Makita')

    search_button = chromium_page.locator("[data-qa='header-search-button']")
    search_button.click()

    product_name_link = chromium_page.locator("[data-qa='product-name']").first
    product_name_link.click()

    brand_name_link = chromium_page.locator("a[class='vzu4Gh']")
    brand_name_link.click()

    brand_image = chromium_page.locator("//img[contains(@class, 'image -show-placeholder')]")
    expect(brand_image).to_be_visible()

    brand_products_listing = chromium_page.locator("div[id='product-listing-top']")
    expect(brand_products_listing).to_be_visible()