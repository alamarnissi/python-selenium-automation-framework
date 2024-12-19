import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":  
        driver = webdriver.Chrome()
        print("launching Chrome browser....")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("launching Firefox browser....")
    else:
        driver = webdriver.Edge()

    driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



