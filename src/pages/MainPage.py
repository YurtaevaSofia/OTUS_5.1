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
    FEATURE_CURRENCY = By.CSS_SELECTOR, "#form-currency > div > button > span"
    FEATURE_EURO = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(1) > button"
    FEATURE_DOLLAR = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(3) > button"
    FEATURE_POUND = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > button"
    FEATURE_PRODUCT_PRICE = By.CSS_SELECTOR, "#content > div.row > div:nth-child(1) > div > div.caption > p.price"


    def go_to_registration_page(self):
        self.browser.find_element(*self.FEATURE_MY_ACCOUNT).click()
        sleep(1)
        self.browser.find_element(*self.FEATURE_REGISTER).click()

    def choose_currency(self, currency):
        self.browser.find_element(*self.FEATURE_CURRENCY).click()
        if currency == "EURO":
            self.browser.find_element(*self.FEATURE_EURO).click()
        if currency == "POUND":
            self.browser.find_element(*self.FEATURE_POUND).click()
        if currency == "DOLLAR":
            self.browser.find_element(*self.FEATURE_DOLLAR).click()
        sleep(1)

    def assert_price(self, price):
        print(self.browser.find_element(*self.FEATURE_PRODUCT_PRICE).text)
        assert(price in self.browser.find_element(*self.FEATURE_PRODUCT_PRICE).text)


