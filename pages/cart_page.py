from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.added_product_card = page.locator("[data-qa='product-item']")
        self.total_price_number = page.locator("[data-qa='checkout-total-total-price']")
        self.create_order_button = page.locator("[data-qa='cart-total-order-create-button']")

    def check_visible_added_product_card(self):
        expect(self.added_product_card).to_be_visible()

    def check_visible_total_price_number(self):
        expect(self.total_price_number).to_be_visible()

    def check_visible_order_button(self):
        expect(self.create_order_button).to_be_visible()
        expect(self.create_order_button).to_have_text('Оформить заказ')