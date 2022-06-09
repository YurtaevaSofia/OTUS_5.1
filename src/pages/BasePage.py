import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        logging.basicConfig(filename="logs.log")
        logging.root.setLevel(logging.INFO)
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(level=logging.INFO)

    def check_element_presence(self, element):
        self.logger.info("Checking element {} presence".format(element))
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(element)
        )

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
