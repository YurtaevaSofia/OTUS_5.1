from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_new_user_page(browser, url):
    link = url + "index.php?route=account/register"
    browser.get(link)

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Wish List"))
        )
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Returns"))
        )
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "login page"))
        )
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Privacy Policy"))
        )
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "content"))
        )

    finally:
        browser.quit()
