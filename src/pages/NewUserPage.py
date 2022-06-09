from time import sleep

from selenium.webdriver.common.by import By

from .BasePage import BasePage


class NewUserPage(BasePage):
    FEATURE_WISH_LIST = By.LINK_TEXT, "Wish List"
    FEATURE_RETURNS = By.LINK_TEXT, "Returns"
    FEATURE_LOGIN_PAGE = By.LINK_TEXT, "login page"
    FEATURE_PRIVATE_POLICY = By.LINK_TEXT, "Privacy Policy"
    FEATURE_CONTENT = By.ID, "content"
    FEATURE_FIRST_NAME = By.CSS_SELECTOR, "#input-firstname"
    FEATURE_LAST_NAME = By.CSS_SELECTOR, "#input-lastname"
    FEATURE_EMAIL = By.CSS_SELECTOR, "#input-email"
    FEATURE_PHONE = By.CSS_SELECTOR, "#input-telephone"
    FEATURE_PASSWORD = By.CSS_SELECTOR, "#input-password"
    FEATURE_CONFIRM_PASSWORD = By.CSS_SELECTOR, "#input-confirm"
    FEATURE_AGREE = By.CSS_SELECTOR, "#form-register > div > div > div > input"
    FEATURE_CONTINUE = By.CSS_SELECTOR, "#form-register > div > div > button"
    FEATURE_USER_IS_REGISTERED = By.CSS_SELECTOR, "#content > h1"

    def fill_in_name(self, first_name, last_name):
        self.logger.info("Enter name and last name")
        self.browser.find_element(*self.FEATURE_FIRST_NAME).send_keys(first_name)
        self.browser.find_element(*self.FEATURE_LAST_NAME).send_keys(last_name)

    def fill_in_email_and_phone(self, email, phone):
        self.logger.info("Enter email and phone")
        self.browser.find_element(*self.FEATURE_EMAIL).send_keys(email)
        #self.browser.find_element(*self.FEATURE_PHONE).send_keys(phone)

    def fill_and_confirm_password(self, password):
        self.logger.info("Enter and confirm password")
        self.browser.find_element(*self.FEATURE_PASSWORD).send_keys(password)
        #self.browser.find_element(*self.FEATURE_CONFIRM_PASSWORD).send_keys(password)

    def agree_to_privacy_policy(self):
        self.logger.info("Agree to privacy policy")
        self.browser.find_element(*self.FEATURE_AGREE).click()
        sleep(1)

    def press_continue_button(self):
        self.logger.info("Click on Continue button")
        self.browser.find_element(*self.FEATURE_CONTINUE).click()
        sleep(3)

    def assert_user_is_registered(self):
        self.logger.info("Assert user is registered")
        assert(self.is_element_present(*self.FEATURE_USER_IS_REGISTERED))


