from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminPage(BasePage):
    FEATURE_FORGOTTEN_PASSWORD = By.LINK_TEXT, "Forgotten Password"
    FEATURE_NAVBAR_BRAND = By.CLASS_NAME, "navbar-brand"
    FEATURE_FAFA_USER = By.CLASS_NAME, "fa.fa-user"
    FEATURE_PASSWORD = By.NAME, "password"
    FEATURE_CONTAINER_FLUID = By.CLASS_NAME, "container-fluid"
    FEATURE_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    FEATURE_CATALOG = By.CSS_SELECTOR, "#menu-catalog > a"
    FEATURE_PRODUCTS = By.CSS_SELECTOR, "#collapse1 > li:nth-child(2)"
    FEATURE_PLUS = By.CSS_SELECTOR, "#content > div.page-header > div > div > a"
    FEATURE_PRODUCT_NAME = By.CSS_SELECTOR, "#input-name1"
    FEATURE_META_TAG_TITLE = By.CSS_SELECTOR, "#input-meta-title1"
    FEATURE_DATA = By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a"
    FEATURE_MODEL = By.CSS_SELECTOR, "#input-model"
    FEATURE_SAVE = By.CSS_SELECTOR, "#content > div.page-header > div > div > button"
    FEATURE_WARNING = By.CSS_SELECTOR, "#content > div.container-fluid > div.alert.alert-danger.alert-dismissible"
    FEATURE_CHECKPOINT = By.CSS_SELECTOR, "input[type=checkbox]"
    FEATURE_DELETE = By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger"


    def login(self):
        self.browser.find_element(*self.FEATURE_LOGIN).click()

    def go_to_products_catalog(self):
        self.browser.find_element(*self.FEATURE_CATALOG).click()
        sleep(1)
        self.browser.find_element(*self.FEATURE_PRODUCTS).click()

    def click_on_plus_button(self):
        self.browser.find_element(*self.FEATURE_PLUS).click()

    def fill_in_new_product_name(self):
        self.browser.find_element(*self.FEATURE_PRODUCT_NAME).send_keys("New product")

    def fill_in_meta_tag_title(self):
        self.browser.find_element(*self.FEATURE_META_TAG_TITLE).send_keys("New tag")

    def fill_in_model(self):
        self.browser.find_element(*self.FEATURE_DATA).click()
        sleep(1)
        self.browser.find_element(*self.FEATURE_MODEL).send_keys("New model")

    def click_on_save_button(self):
        self.browser.find_element(*self.FEATURE_SAVE).click()
        sleep(2)

    def assert_warning_is_displayed(self):
        assert(self.is_element_present(*self.FEATURE_WARNING))
        sleep(2)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def select_one_element(self):
        self.browser.find_element(*self.FEATURE_CHECKPOINT).click()
        sleep(3)

    def click_on_delete_button(self):
        self.browser.find_element(*self.FEATURE_DELETE).click()
        sleep(2)

