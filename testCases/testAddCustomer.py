import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomerPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import LogHandler
from utilities.randomGen import RandomGenerator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test_003_AddCustomer:
    baseUrl = ReadProperties.getApplicationURL()
    username = ReadProperties.getUsername()
    password = ReadProperties.getPassword()

    logger = LogHandler.loggen()

    def test_addCustomer(self, setup):
        self.logger.info("********* Test_003_AddCustomer *********")
        self.logger.info("********* Started Add Customer Test *********")
        self.driver = setup
        self.driver.get(self.baseUrl)       ## start browser with base url
        wait = WebDriverWait(self.driver, 10)
        self.loginPage = LoginPage(self.driver)   ## instance of Login page
        self.addCustomerPage = AddCustomerPage(self.driver)    ## instance of AddCustomer page

        ## start login flow
        time.sleep(2)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        time.sleep(1)
        self.loginPage.clickLogin()
        time.sleep(5)
        modalBtn = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[1]/div/div[3]/span")
            
        if modalBtn.is_displayed():
            modalBtn.click()
            # Here i'm waiting for the modal to disappear before clicking the logout link
            wait.until(
                EC.invisibility_of_element((By.CLASS_NAME, "modal-backdrop"))
            )
        self.logger.info("************* Login succesful **********")
        time.sleep(5)

        ## start add customer flow
        self.logger.info("******* Starting Add Customer Test **********")
        self.addCustomerPage.clickOnCustomersMenu()
        self.addCustomerPage.clickOnCustomersMenuItem()
        self.addCustomerPage.clickOnAddnew()

        self.randomEmail = RandomGenerator() + "@gmail.com"
        self.addCustomerPage.setEmail(self.randomEmail)
        self.addCustomerPage.setPassword("testcustomer123")
        self.addCustomerPage.setFirstName("testcustomer")
        self.addCustomerPage.setLastName("lastname")
        self.addCustomerPage.setGender("male")
        self.addCustomerPage.setDateOfBirth("05/10/1980")    # Format: mm / dd / yyyy
        self.addCustomerPage.setCompanyName("test company")
        self.addCustomerPage.setCustomerRoles("Registered")
        self.addCustomerPage.setManagerOfVendor("Vendor 1")
        self.addCustomerPage.setAdminContent("This is admin content")

        self.addCustomerPage.clickOnSave()
        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.TAGNAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")



