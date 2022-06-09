from time import sleep
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from .BasePage import BasePage


class AdminPage(BasePage):
    FEATURE_FORGOTTEN_PASSWORD = By.LINK_TEXT, "Forgotten Password"
    FEATURE_NAVBAR_BRAND = By.CLASS_NAME, "navbar-brand"
    FEATURE_FAFA_USER = By.CLASS_NAME, "card"
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
    FEATURE_EMAIL = By.ID, "input-username"
    FEATURE_PASSWORD = By.ID, "input-password"



    def login(self):
        self.logger.info("Click on button Login")
        self.browser.find_element(*self.FEATURE_LOGIN).click()

    def go_to_products_catalog(self):
        self.logger.info("Go to products catalog")
        self.browser.find_element(*self.FEATURE_CATALOG).click()
        self.browser.find_element(*self.FEATURE_PRODUCTS).click()

    def enter_email_and_password(self):
        self.logger.info("Enter email for registration")
        self.browser.find_element(*self.FEATURE_EMAIL).send_keys("test2@mail.ru")
        self.logger.info("Enter password")
        self.browser.find_element(*self.FEATURE_PASSWORD).send_keys("test")
        sleep(5)

    def click_on_plus_button(self):
        self.logger.info("Click on adding button")
        self.browser.find_element(*self.FEATURE_PLUS).click()

    def fill_in_new_product_name(self):
        self.logger.info("Enter new product name")
        self.browser.find_element(*self.FEATURE_PRODUCT_NAME).send_keys("New product")

    def fill_in_meta_tag_title(self):
        self.logger.info("Enter new product tag")
        self.browser.find_element(*self.FEATURE_META_TAG_TITLE).send_keys("New tag")

    def fill_in_model(self):
        self.browser.find_element(*self.FEATURE_DATA).click()
        sleep(1)
        self.logger.info("Enter model")
        self.browser.find_element(*self.FEATURE_MODEL).send_keys("New model")

    def click_on_save_button(self):
        self.logger.info("Click on Save button")
        self.browser.find_element(*self.FEATURE_SAVE).click()
        sleep(2)

    def assert_warning_is_displayed(self):
        self.logger.info("Assert warning is displayed")
        assert(self.is_element_present(*self.FEATURE_WARNING))
        sleep(2)

    def select_one_element(self):
        self.browser.find_element(*self.FEATURE_CHECKPOINT).click()
        sleep(3)

    def click_on_delete_button(self):
        self.logger.info("Click on Delete button")
        self.browser.find_element(*self.FEATURE_DELETE).click()
        sleep(2)

    def accept_alert(self):
        self.logger.info("Accept alert")
        alert = WebDriverWait(self.browser, 2).until(EC.alert_is_present())
        alert.accept()
