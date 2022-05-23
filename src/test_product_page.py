from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page(browser, url):
    link = url + "index.php?route=product/product&path=20&product_id=30"
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "container"))
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Description"))
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Write a review"))
    )
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Canon"))
    )

