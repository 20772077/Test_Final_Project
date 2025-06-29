from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import *

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert  self.url in self.browser.current_url, f"URL is wrong: {self.browser.current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_PAGE_LINK), "Login email input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_PAGE_LINK), "Login password input is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_PAGE_LINK), "Register email input is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_PAGE_LINK), "Register password input is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_REPEAT_PASSWORD_PAGE_LINK), "Register repeat password input is not presented"
        