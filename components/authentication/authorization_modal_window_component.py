from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import allure

class AuthorizationModalWindowComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.locator("[data-qa='login']")
        self.submit_login_button = page.locator("[data-qa='submit']")
        self.password_input = page.locator("[data-qa='password']")
        self.submit_password_button = page.locator("[data-qa='submit']")

    def check_visible_email_input(self):
        with allure.step('Checking that email input is visible'):
            expect(self.email_input).to_be_visible()

    def fill_email_input(self, email: str):
        with allure.step(f'Filling email input with email: {email}'):
            self.email_input.type(text=f'{email}', delay=350)
            expect(self.email_input).to_have_value(email)

    def click_submit_login_button(self):
        with allure.step('Clicking button "Submit login"'):
            self.submit_login_button.click()

    def check_visible_password_input(self):
        with allure.step('Checking that password input is visible'):
            self.page.wait_for_timeout(1000)
            expect(self.password_input).to_be_visible()

    def fill_password_input(self, password: str):
        with allure.step(f'Filling password input with password: {password}'):
            self.password_input.type(text=f'{password}', delay=350)

    def click_submit_password_button(self):
        with allure.step('Clicking button "Submit password"'):
            self.submit_password_button.click()