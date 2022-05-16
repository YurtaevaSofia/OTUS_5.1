from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_page(browser, url):
    link = url + "admin/"
    browser.get(link)

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Forgotten Password"))
        )
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "navbar-brand")),
        )
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fa.fa-user"))
        )
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "container-fluid"))
        )


    finally:
        browser.quit()