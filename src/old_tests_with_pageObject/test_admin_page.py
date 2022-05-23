from src.pages.AdminPage import AdminPage


def test_admin_page(browser, url):
    link = url + "admin/"
    browser.get(link)
    AdminPage(browser).check_element_presence(AdminPage.FEATURE_PASSWORD)
    AdminPage(browser).check_element_presence(AdminPage.FEATURE_NAVBAR_BRAND)
    AdminPage(browser).check_element_presence(AdminPage.FEATURE_FAFA_USER)
    AdminPage(browser).check_element_presence(AdminPage.FEATURE_CONTAINER_FLUID)
    AdminPage(browser).check_element_presence(AdminPage.FEATURE_FORGOTTEN_PASSWORD)


def test_add_new_product(browser, url):
    link = url + "admin/"
    browser.get(link)
    AdminPage(browser).login()
    AdminPage(browser).go_to_products_catalog()
    AdminPage(browser).click_on_plus_button()
    AdminPage(browser).fill_in_new_product_name()
    AdminPage(browser).fill_in_meta_tag_title()
    AdminPage(browser).fill_in_model()
    AdminPage(browser).click_on_save_button()
    AdminPage(browser).assert_warning_is_displayed()


def test_delete_new_product(browser, url):
    link = url + "admin/"
    browser.get(link)
    AdminPage(browser).login()
    AdminPage(browser).go_to_products_catalog()
    AdminPage(browser).select_one_element()
    AdminPage(browser).click_on_delete_button()
    AdminPage(browser).accept_alert()
    AdminPage(browser).assert_warning_is_displayed()











