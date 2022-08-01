import random
import string

from src.pages.AdminPage import AdminPage
from src.pages.MainPage import MainPage
from src.pages.NewUserPage import NewUserPage


def test_add_new_product(browser, url):
    link = url + "admin/"
    browser.get(link)
    
