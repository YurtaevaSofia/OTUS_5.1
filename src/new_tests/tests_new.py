import random
import string

from src.pages.AdminPage import AdminPage
from src.pages.MainPage import MainPage
from src.pages.NewUserPage import NewUserPage


def test_add_new_product(browser, url):
    link = url + "admin/"
    browser.get(link)
    AdminPage(browser).login()
    AdminPage(browser).enter_email_and_password()
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


def test_register_new_user(browser, url):
    link = url
    browser.get(link)
    MainPage(browser).go_to_registration_page()
    NewUserPage(browser).fill_in_name("Test", "Test")
    NewUserPage(browser).fill_in_email_and_phone(email_generator() + "@mail.ru", "89999999999")
    NewUserPage(browser).fill_and_confirm_password("test_password")
    NewUserPage(browser).agree_to_privacy_policy()
    NewUserPage(browser).press_continue_button()
    NewUserPage(browser).assert_user_is_registered()


def email_generator(chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(6))


def test_assert_price(browser, url):
    link = url
    browser.get(link)
    MainPage(browser).choose_currency("EURO")
    MainPage(browser).assert_price("592")
    MainPage(browser).choose_currency("POUND")
    MainPage(browser).assert_price("501")
    MainPage(browser).choose_currency("DOLLAR")
    MainPage(browser).assert_price("602")

