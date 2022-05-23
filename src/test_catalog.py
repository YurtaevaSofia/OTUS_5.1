from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page(browser, url):
    link = url + "index.php?route=product/category&path=20"
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Desktops")),
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "top-links"))
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "container"))
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Tablets"))
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Cameras"))
    )
