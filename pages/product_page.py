from pages.base_page import BasePage
from playwright.sync_api import Page, expect
import allure

class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.product_title = page.locator("[data-qa='get-product-title']")
        self.current_price = page.locator("[data-qa='price-now']")
        self.add_to_cart_button = page.locator("[data-qa='add-to-cart-btn']")
        self.brand_image_link = page.locator("a[class='vzu4Gh']")

    def check_visible_product_title(self):
        with allure.step('Checking that product title is visible'):
            expect(self.product_title).to_be_visible()

    def check_visible_current_price(self):
        with allure.step('Checking that current price is visible'):
            expect(self.current_price).to_be_visible()

    def check_visible_add_to_cart_button(self):
        with allure.step('Checking that add to cart button is visible'):
            expect(self.add_to_cart_button).to_be_visible()
            expect(self.add_to_cart_button).to_have_text('В корзину')

    def click_add_to_cart_button(self):
        with allure.step('Clicking button "Add to cart"'):
            self.add_to_cart_button.click()

    def click_brand_image_link(self):
        with allure.step('Clicking on the brand image'):
            self.brand_image_link.click()