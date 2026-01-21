import pytest
import allure

from config import settings
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

@pytest.mark.cidemo
class TestCIDemo:
    @allure.title('User login with valid email and password')
    @allure.epic(AllureEpic.CONSUMER)
    @allure.feature(AllureFeature.AUTHENTICATION)
    @allure.story(AllureStory.AUTHORIZATION)
    def test_authorization(self, catalog_page: CatalogPage):
        catalog_page.visit("/")
        catalog_page.check_page_have_title()


    @allure.title('Search for existing item')
    @allure.epic(AllureEpic.CONSUMER)
    @allure.feature(AllureFeature.SEARCH)
    @allure.story(AllureStory.SEARCH)
    def test_search_for_product(self, catalog_page: CatalogPage):
        catalog_page.visit("/")
        catalog_page.check_page_have_title()


    @allure.title('Adding item to shopping cart and navigation to cart page')
    @allure.epic(AllureEpic.CONSUMER)
    @allure.feature(AllureFeature.CART)
    @allure.story(AllureStory.CART)
    def test_adding_product_to_cart(self, catalog_page: CatalogPage, cart_page: CartPage):
        catalog_page.visit("/")
        catalog_page.check_page_have_title()