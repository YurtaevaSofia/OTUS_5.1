from src.pages.ProductPage import ProductPage


def test_product_page(browser, url):
    link = url + "index.php?route=product/product&path=20&product_id=30"
    browser.get(link)

    ProductPage(browser).check_element_presence(ProductPage.FEATURE_CONTAINER)
    ProductPage(browser).check_element_presence(ProductPage.FEATURE_CONTENT)
    ProductPage(browser).check_element_presence(ProductPage.FEATURE_CANON)
    ProductPage(browser).check_element_presence(ProductPage.FEATURE_DESCRIPTION)
    ProductPage(browser).check_element_presence(ProductPage.FEATURE_WRITE_A_REVIEW)
