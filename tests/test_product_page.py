import pytest
from pages.product_page import ProductPage
from pages.catalog_page import CatalogPage

@pytest.mark.smoke
@pytest.mark.regression
def test_product_page_elements(product_page: ProductPage, catalog_page: CatalogPage):
    catalog_page.visit('https://www.vseinstrumenti.ru/')
    catalog_page.fill_search_field(search_string='кусторез DeWalt')
    catalog_page.click_search_button()
    catalog_page.click_first_results_tile()
    product_page.check_visible_product_title()
    product_page.check_visible_current_price()
    product_page.check_visible_add_to_cart_button()
    product_page.click_add_to_cart_button()