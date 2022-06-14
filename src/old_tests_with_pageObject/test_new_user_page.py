from src.pages.NewUserPage import NewUserPage


def test_new_user_page(browser, url):
    link = url + "index.php?route=account/register"
    browser.get(link)

    NewUserPage(browser).check_element_presence(NewUserPage.FEATURE_LOGIN_PAGE)
    NewUserPage(browser).check_element_presence(NewUserPage.FEATURE_CONTENT)
    NewUserPage(browser).check_element_presence(NewUserPage.FEATURE_RETURNS)
    NewUserPage(browser).check_element_presence(NewUserPage.FEATURE_PRIVATE_POLICY)
    NewUserPage(browser).check_element_presence(NewUserPage.FEATURE_WISH_LIST)
