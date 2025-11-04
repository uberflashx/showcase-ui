from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CatalogPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.search_input = page.locator("[data-qa='header-search-input']")
        self.search_button = page.locator("[data-qa='header-search-button']")
        self.search_results_tiles = page.locator("[data-qa='listing']")
        self.first_results_tile = page.locator("[data-qa='products-tile']").first

    def fill_search_field(self, search_string: str):
        self.search_input.fill(search_string)
        expect(self.search_input).to_have_value(search_string)

    def click_search_button(self):
        self.search_button.click()

    def check_visible_results_tiles(self):
        expect(self.search_results_tiles).to_be_visible()

    def click_first_results_tile(self):
        self.first_results_tile.click()
