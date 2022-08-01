from src.pages.AdminPage import AdminPage
import allure

@allure.feature('Admin_page_check')
@allure.title('Check elements on Admin_page')
def test_admin_page(browser, url):
    link = url + "admin/"
    browser.get(link)
    AdminPage(browser).check_element_presence(AdminPage.FEATURE_PASSWORD)
    AdminPage(browser).check_element_presence(AdminPage.FEATURE_NAVBAR_BRAND)
    AdminPage(browser).check_element_presence(AdminPage.FEATURE_FAFA_USER)
    AdminPage(browser).check_element_presence(AdminPage.FEATURE_CONTAINER_FLUID)
    AdminPage(browser).check_element_presence(AdminPage.FEATURE_FORGOTTEN_PASSWORD)
