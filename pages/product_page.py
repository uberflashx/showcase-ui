from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.product_title = page.locator("[data-qa='get-product-title']")
        self.current_price = page.locator("[data-qa='price-now']")
        self.add_to_cart_button = page.locator("[data-qa='add-to-cart-btn']")

    def check_visible_product_title(self):
        expect(self.product_title).to_be_visible()

    def check_visible_current_price(self):
        expect(self.current_price).to_be_visible()

    def check_visible_add_to_cart_button(self):
        expect(self.add_to_cart_button).to_be_visible()
        expect(self.add_to_cart_button).to_have_text('В корзину')

    def click_add_to_cart_button(self):
        self.add_to_cart_button.click()