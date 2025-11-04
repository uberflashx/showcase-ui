import pytest
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.brand_page import BrandPage

@pytest.mark.regression
def test_brand_page_elements(catalog_page: CatalogPage, product_page: ProductPage, brand_page: BrandPage):
    catalog_page.visit('https://www.vseinstrumenti.ru/')
    catalog_page.fill_search_field(search_string='газонокосилка Makita')
    catalog_page.click_search_button()
    catalog_page.click_first_results_tile()
    product_page.click_brand_image_link()
    brand_page.check_visible_brand_image()
    brand_page.check_visible_brand_products_listing()