from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser, url):
    link = url
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "search")),
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "cart-total"))
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "container"))
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "img-responsive"))
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Your Store"))
    )