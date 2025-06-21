from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class  LoginPageLocators():
    LOGIN_EMAIL_PAGE_LINK = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_PAGE_LINK = (By.CSS_SELECTOR, "#id_login-password")

    REGISTER_EMAIL_PAGE_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_PAGE_LINK = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_REPEAT_PASSWORD_PAGE_LINK = (By.CSS_SELECTOR, "#id_registration-password1")
