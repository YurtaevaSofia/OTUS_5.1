import logging

from selenium import webdriver

from selenium.webdriver.opera.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Choose browser")
    parser.addoption("--executor", action="store", default="local")

    parser.addoption(
        "--url",
        default="https://demo.opencart.com/",
        help="This is request url"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    # if browser_name == "chrome":
    #     print("Using Chrome browser")
    #     browser = webdriver.Chrome()
    # elif browser_name == "firefox":
    #     print("Using Firefox browser")
    #     browser = webdriver.Firefox()
    # elif browser_name == "Opera":
    #     print("Using Opera browser")
    #     browser = webdriver.Opera()
    # else:
    #     raise pytest.UsageError("--browser should be chrome or firefox or Opera")

    options = webdriver.ChromeOptions()
    options.set_capability("loggingPrefs", {'performance': 'ALL'})
    
    if executor == "local":
        caps = {'goog:chromeOptions': {}}
        driver = webdriver.Chrome(desired_capabilities=caps)

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser_name
        }

        options = Options()
        if browser_name == "opera":
            options.add_experimental_option('w3c', True)

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
            options=options
        )

        driver.maximize_window()

    yield driver
    print("Quiting browser..")
    driver.quit()


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


def exception_case(self, exception, driver):
    logging.error(f'Exception accused: {exception}')
    driver.save_screenshot(f'{exception}.png')
