import pytest
import allure
from pages.catalog_page import CatalogPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

@pytest.mark.smoke
@pytest.mark.search
@pytest.mark.regression
@allure.title('Search for existing item')
@allure.epic(AllureEpic.CONSUMER)
@allure.feature(AllureFeature.SEARCH)
@allure.story(AllureStory.SEARCH)
def test_search_for_product(catalog_page: CatalogPage):
    catalog_page.visit('https://www.vseinstrumenti.ru/')
    catalog_page.fill_search_field(search_string='газонокосилка Makita')
    catalog_page.click_search_button()
    catalog_page.check_visible_results_tiles()