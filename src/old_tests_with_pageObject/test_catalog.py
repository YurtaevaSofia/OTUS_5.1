from src.pages.CatalogPage import CatalogPage


def test_catalog_page(browser, url):
    link = url + "index.php?route=product/category&path=20"
    browser.get(link)

    CatalogPage(browser).check_element_presence(CatalogPage.FEATURE_CONTAINER)
    CatalogPage(browser).check_element_presence(CatalogPage.FEATURE_TOP_LINKS)
    CatalogPage(browser).check_element_presence(CatalogPage.FEATURE_CAMERAS)
    CatalogPage(browser).check_element_presence(CatalogPage.FEATURE_TABLETS)
    CatalogPage(browser).check_element_presence(CatalogPage.FEATURE_DESKTOPS)


