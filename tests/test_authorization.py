import pytest
import allure
from pages.catalog_page import CatalogPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

@pytest.mark.regression
@allure.title('User login with valid email and password')
@allure.epic(AllureEpic.CONSUMER)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
def test_authorization(catalog_page: CatalogPage):
    catalog_page.visit('https://www.vseinstrumenti.ru/')
    catalog_page.check_visible_login_button()
    catalog_page.click_login_button()
    catalog_page.auth_modal_window.check_visible_email_input()
    catalog_page.auth_modal_window.fill_email_input(email='ttlscrt22@gmail.com')
    catalog_page.auth_modal_window.click_submit_login_button()
    catalog_page.auth_modal_window.check_visible_password_input()
    catalog_page.auth_modal_window.fill_password_input(password='pa$$w0rd')
    catalog_page.auth_modal_window.click_submit_password_button()
    catalog_page.check_visible_user_menu()