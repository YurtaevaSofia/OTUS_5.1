from selenium.webdriver.common.by import By

from .BasePage import BasePage


class CatalogPage(BasePage):
    FEATURE_DESKTOPS = By.LINK_TEXT, "Desktops"
    FEATURE_TOP_LINKS = By.ID, "top"
    FEATURE_CONTAINER = By.CLASS_NAME, "container"
    FEATURE_TABLETS = By.LINK_TEXT, "Tablets"
    FEATURE_CAMERAS = By.LINK_TEXT, "Cameras"






