from time import sleep

from selenium.webdriver.common.by import By

from .BasePage import BasePage


class MainPage(BasePage):
    FEATURE_SEARCH = (By.NAME, "search")
    FEATURE_CART_TOTAL = (By.ID, "cart-total")
    FEATURE_CONTAINER = (By.CLASS_NAME, "container")
    FEATURE_IMG = (By.CLASS_NAME, "img-responsive")
    FEATURE_YOUR_STORE = (By.LINK_TEXT, "Your Store")
    FEATURE_MY_ACCOUNT = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md")
    FEATURE_REGISTER = (By.LINK_TEXT, "Register")

    def go_to_registration_page(self):
        self.browser.find_element(*self.FEATURE_MY_ACCOUNT).click()
        sleep(1)
        self.browser.find_element(*self.FEATURE_REGISTER).click()

