import pytest
from pages.catalog_page import CatalogPage

@pytest.mark.regression
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