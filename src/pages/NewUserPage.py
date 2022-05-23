from selenium.webdriver.common.by import By

from .BasePage import BasePage


class NewUserPage(BasePage):
    FEATURE_WISH_LIST = By.LINK_TEXT, "Wish List"
    FEATURE_RETURNS = By.LINK_TEXT, "Returns"
    FEATURE_LOGIN_PAGE = By.LINK_TEXT, "login page"
    FEATURE_PRIVATE_POLICY = By.LINK_TEXT, "Privacy Policy"
    FEATURE_CONTENT = By.ID, "content"




