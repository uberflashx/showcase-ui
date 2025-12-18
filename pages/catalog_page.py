from asyncio import wait_for
import allure

from components.authentication.authorization_modal_window_component import AuthorizationModalWindowComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CatalogPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.auth_modal_window = AuthorizationModalWindowComponent(page)

        self.search_input = page.locator("[data-qa='header-search-input']")
        self.search_button = page.locator("[data-qa='header-search-button']")
        self.search_results_tiles = page.locator("[data-qa='listing']")
        self.first_results_tile = page.locator("[data-qa='products-tile']").first
        self.product_tile_cart_button = page.locator("[data-qa='product-add-to-cart-button']").first
        self.pupup_go_to_cart_button = page.locator("[data-qa='go-to-basket']")

        self.login_button = page.locator("[data-qa='login-and-registration']")
        self.user_menu = page.locator("[data-qa='user-menu']")

    def fill_search_field(self, search_string: str):
        with allure.step(f'Filling search input with search string: {search_string}'):
            self.search_input.fill(search_string)
            expect(self.search_input).to_have_value(search_string)

    def click_search_button(self):
        with allure.step('Clicking button "Search"'):
            self.search_button.click()

    def check_visible_results_tiles(self):
        with allure.step('Checking that results tiles are visible'):
            expect(self.search_results_tiles).to_be_visible()

    def click_first_results_tile(self):
        with allure.step('Clicking on the first results tile'):
            self.first_results_tile.click()

    def click_tile_add_to_cart_button(self):
        with allure.step('Clicking button "Add to cart"'):
            self.product_tile_cart_button.click()

    def click_pupup_go_to_cart_button(self):
        with allure.step('Clicking button "Go to cart"'):
            self.pupup_go_to_cart_button.click()

    def check_visible_login_button(self):
        with allure.step('Checking that login button is visible'):
            expect(self.login_button).to_be_visible()

    def click_login_button(self):
        with allure.step('Clicking button "Login"'):
            self.login_button.click()

    def check_visible_user_menu(self):
        with allure.step('Checking that username is visible'):
            expect(self.user_menu).to_be_visible()