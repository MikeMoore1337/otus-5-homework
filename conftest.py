import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser for run tests")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("C:/drivers/"), help="path to drivers")
    parser.addoption("--url", action="store", default="http://192.168.1.59:8081/", help="default url")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    url = request.config.getoption("--url")

    if browser == "chrome":
        service = ChromiumService(executable_path=drivers + "/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver.exe")
        driver = webdriver.Firefox(service=service)
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver.exe")
    elif browser == "edge":
        driver = webdriver.Edge(executable_path=drivers + "/msedgedriver.exe")
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Browser {browser} is not supported.")

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
