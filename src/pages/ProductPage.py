from selenium.webdriver.common.by import By

from .BasePage import BasePage


class ProductPage(BasePage):
    FEATURE_CONTENT = By.ID, "content"
    FEATURE_DESCRIPTION = By.LINK_TEXT, "Description"
    FEATURE_CONTAINER = (By.CLASS_NAME, "container")
    FEATURE_WRITE_A_REVIEW = By.LINK_TEXT, "Write a review"
    FEATURE_CANON = By.LINK_TEXT, "Canon"




