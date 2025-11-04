from asyncio import wait_for

from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CatalogPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.search_input = page.locator("[data-qa='header-search-input']")
        self.search_button = page.locator("[data-qa='header-search-button']")
        self.search_results_tiles = page.locator("[data-qa='listing']")
        self.first_results_tile = page.locator("[data-qa='products-tile']").first
        self.product_tile_cart_button = page.locator("[data-qa='product-add-to-cart-button']").first
        self.pupup_go_to_cart_button = page.locator("[data-qa='go-to-basket']")

        self.login_button = page.locator("[data-qa='login-and-registration']")
        self.email_input = page.locator("[data-qa='login']")
        self.submit_login_button = page.locator("[data-qa='submit']")
        self.password_input = page.locator("[data-qa='password']")
        self.submit_password_button = page.locator("[data-qa='submit']")
        self.user_menu = page.locator("[data-qa='user-menu']")

    def fill_search_field(self, search_string: str):
        self.search_input.fill(search_string)
        expect(self.search_input).to_have_value(search_string)

    def click_search_button(self):
        self.search_button.click()

    def check_visible_results_tiles(self):
        expect(self.search_results_tiles).to_be_visible()

    def click_first_results_tile(self):
        self.first_results_tile.click()

    def click_tile_add_to_cart_button(self):
        self.product_tile_cart_button.click()

    def click_pupup_go_to_cart_button(self):
        self.pupup_go_to_cart_button.click()

    def check_visible_login_button(self):
        expect(self.login_button).to_be_visible()

    def click_login_button(self):
        self.login_button.click()

    def check_visible_email_input(self):
        expect(self.email_input).to_be_visible()

    def fill_email_input(self, email: str):
        self.email_input.type(text=f'{email}', delay=350)
        expect(self.email_input).to_have_value(email)

    def click_submit_login_button(self):
        self.submit_login_button.click()

    def check_visible_password_input(self):
        self.page.wait_for_timeout(3000)
        expect(self.password_input).to_be_visible()

    def fill_password_input(self, password: str):
        self.password_input.type(text=f'{password}', delay=350)

    def click_submit_password_button(self):
        self.submit_password_button.click()

    def check_visible_user_menu(self):
        expect(self.user_menu).to_be_visible()