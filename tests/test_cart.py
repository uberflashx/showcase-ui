import pytest
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage

@pytest.mark.regression
def test_adding_product_to_cart(catalog_page: CatalogPage, cart_page: CartPage):
    catalog_page.visit('https://www.vseinstrumenti.ru/')
    catalog_page.fill_search_field(search_string='газонокосилка Makita')
    catalog_page.click_search_button()
    catalog_page.click_tile_add_to_cart_button()
    catalog_page.click_pupup_go_to_cart_button()
    cart_page.check_visible_added_product_card()
    cart_page.check_visible_total_price_number()
    cart_page.check_visible_order_button()