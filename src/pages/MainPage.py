from selenium.webdriver.common.by import By

from .BasePage import BasePage


class MainPage(BasePage):
    FEATURE_SEARCH = (By.NAME, "search")
    FEATURE_CART_TOTAL = (By.ID, "cart-total")
    FEATURE_CONTAINER = (By.CLASS_NAME, "container")
    FEATURE_IMG = (By.CLASS_NAME, "img-responsive")
    FEATURE_YOUR_STORE = (By.LINK_TEXT, "Your Store")




