from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def check_element_presence(self, element):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(element)
        )

