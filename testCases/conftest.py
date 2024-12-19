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

def pytest_addoption(parser):   # this will get the value from CLI
    parser.addoption("--browser")  # this will get the value of --browser from CLI

@pytest.fixture()
def browser(request):         # this will return the browser value to setup method
    return request.config.getoption("--browser")



