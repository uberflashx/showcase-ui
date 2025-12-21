from pages.base_page import BasePage
from playwright.sync_api import Page, expect
import allure

class BrandPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.brand_image = page.locator("//img[contains(@class, 'image -show-placeholder')]")
        self.brand_products_listing = page.locator("div[id='product-listing-top']")

    def check_visible_brand_image(self):
        with allure.step('Checking that brand image is visible'):
            expect(self.brand_image).to_be_visible()

    def check_visible_brand_products_listing(self):
        with allure.step('Checking that brand products are visible'):
            expect(self.brand_products_listing).to_be_visible()