from src.pages.MainPage import MainPage


def test_main_page(browser, url):
    link = url
    browser.get(link)

    MainPage(browser).check_element_presence(MainPage.FEATURE_SEARCH)
    MainPage(browser).check_element_presence(MainPage.FEATURE_CART_TOTAL)
    MainPage(browser).check_element_presence(MainPage.FEATURE_IMG)
    MainPage(browser).check_element_presence(MainPage.FEATURE_CONTAINER)
    MainPage(browser).check_element_presence(MainPage.FEATURE_CHECKOUT)
