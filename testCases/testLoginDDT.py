
import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import LogHandler
import utilities.excelUtils as excel

class Test_002_login_DDT:
    baseUrl = ReadProperties.getApplicationURL()
    path = ".\\TestData/LoginData.xlsx"

    logger = LogHandler.loggen()

    def test_login(self, setup):
        self.logger.info("********* Test_002_login_DDT *********")
        self.logger.info("********* Started Login DDT Test *********")
        self.driver = setup
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.baseUrl)
        self.loginPage = LoginPage(self.driver)  ## instance of login page

        self.countRows = excel.getRowCount(self.path, "Sheet1")

        listStatus = []

        for r in range(2,self.countRows+1):
            self.username = excel.readData(self.path, "Sheet1", r, 1)
            self.password = excel.readData(self.path, "Sheet1", r, 2)
            self.expected = excel.readData(self.path, "Sheet1", r, 3)

            self.loginPage.setUserName(self.username)
            self.loginPage.setPassword(self.password)
            self.loginPage.clickLogin()
            time.sleep(4)
            actual_title = self.driver.title

            if actual_title == "Dashboard / nopCommerce administration":
                modalBtn = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[4]/div[1]/div/div[3]/span")
            
                if modalBtn.is_displayed():
                    modalBtn.click()
                    # Here i'm waiting for the modal to disappear before clicking the logout link
                    wait.until(
                        EC.invisibility_of_element((By.CLASS_NAME, "modal-backdrop"))
                    )
                if self.expected == "Pass":
                    self.loginPage.clickLogout()
                    self.logger.info("********* PASSED *********")
                    listStatus.append("Pass")
                elif self.expected == "Fail":
                    self.loginPage.clickLogout()
                    self.logger.info("********* FAILED *********")
                    listStatus.append("Fail")
            else:
                if self.expected == "Pass":
                    self.logger.info("********* FAILED *********")
                    listStatus.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("********* PASSED *********")
                    listStatus.append("Pass")

        if "Fail" not in listStatus:
            self.logger.info("********* Login DDT Test Passed *********")
            self.driver.close()
            assert True
        else:
            self.logger.error("********* Login DDT Test Failed *********")
            self.driver.close()
            assert False
        
        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed Test_002_login_DDT ************* ");


