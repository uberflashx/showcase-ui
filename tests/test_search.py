import pytest
from pages.catalog_page import CatalogPage

@pytest.mark.smoke
@pytest.mark.search
def test_search_for_product(catalog_page: CatalogPage):
    catalog_page.visit('https://www.vseinstrumenti.ru/')
    catalog_page.fill_search_field(search_string='газонокосилка Makita')
    catalog_page.click_search_button()
    catalog_page.check_visible_results_tiles()