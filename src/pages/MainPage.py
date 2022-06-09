from time import sleep

from selenium.webdriver.common.by import By

from .BasePage import BasePage


class MainPage(BasePage):
    FEATURE_SEARCH = (By.NAME, "search")
    FEATURE_CART_TOTAL = (By.ID, "wishlist-total")
    FEATURE_CONTAINER = (By.CLASS_NAME, "container")
    FEATURE_IMG = (By.CLASS_NAME, "img-fluid")
    FEATURE_CHECKOUT = (By.LINK_TEXT, "Checkout")
    FEATURE_MY_ACCOUNT = (By.CSS_SELECTOR, "#top > div.container > div.nav.float-end > ul > li:nth-child(2) > div > a > span")
    FEATURE_REGISTER = (By.LINK_TEXT, "Register")
    FEATURE_CURRENCY = By.CSS_SELECTOR, "#form-currency > div > a > span"
    FEATURE_EURO = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(1) > a"
    FEATURE_DOLLAR = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(3) > a"
    FEATURE_POUND = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > a"
    FEATURE_PRODUCT_PRICE = By.CSS_SELECTOR, "#content > div.row > div:nth-child(1) > form > div > div.content > div.description > div > span.price-new"


    def go_to_registration_page(self):
        sleep(1)
        self.browser.find_element(*self.FEATURE_MY_ACCOUNT).click()
        self.browser.find_element(*self.FEATURE_REGISTER).click()
        self.logger.info("Go to register page")

    def choose_currency(self, currency):
        self.logger.info("Choosing currency")
        sleep(1)
        self.browser.find_element(*self.FEATURE_CURRENCY).click()
        if currency == "EURO":
            self.browser.find_element(*self.FEATURE_EURO).click()
        if currency == "POUND":
            self.browser.find_element(*self.FEATURE_POUND).click()
        if currency == "DOLLAR":
            self.browser.find_element(*self.FEATURE_DOLLAR).click()
        sleep(1)

    def assert_price(self, price):
        self.logger.info("Assert price")
        print(self.browser.find_element(*self.FEATURE_PRODUCT_PRICE).text)
        assert(price in self.browser.find_element(*self.FEATURE_PRODUCT_PRICE).text)


