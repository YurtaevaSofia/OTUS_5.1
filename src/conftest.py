from selenium import webdriver

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Choose browser"
    )
    parser.addoption(
        "--url",
        default="https://demo.opencart.com/",
        help="This is request url"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser_name == "chrome":
        print("Using Chrome browser")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("Using Firefox browser")
        browser = webdriver.Firefox()
    elif browser_name == "Opera":
        print("Using Opera browser")
        browser = webdriver.Opera()
    else:
        raise pytest.UsageError("--browser should be chrome or firefox or Opera")
    yield browser
    print("Quiting browser..")
    browser.quit()


@pytest.fixture
def url(request):
    return request.config.getoption("--url")

