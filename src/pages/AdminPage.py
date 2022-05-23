from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminPage(BasePage):
    FEATURE_FORGOTTEN_PASSWORD = By.LINK_TEXT, "Forgotten Password"
    FEATURE_NAVBAR_BRAND = By.CLASS_NAME, "navbar-brand"
    FEATURE_FAFA_USER = By.CLASS_NAME, "fa.fa-user"
    FEATURE_PASSWORD = By.NAME, "password"
    FEATURE_CONTAINER_FLUID = By.CLASS_NAME, "container-fluid"
