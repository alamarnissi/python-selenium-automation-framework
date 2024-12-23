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


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Project Name": "nop Commerce",
        "Module Name": "Customers",
        "Tester":"Marnissi"
    }

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



