
import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import LogHandler

class Test_001_login:
    baseUrl = ReadProperties.getApplicationURL()
    username = ReadProperties.getUsername()
    password = ReadProperties.getPassword()

    logger = LogHandler.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("********* Test_001_login **********")
        self.logger.info("********* Started Home Page Title Test *********")
        self.driver = setup
        self.logger.info("**** Opening URL ****")
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            self.logger.info("********* Test Home Page Title PASSED *********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("********* Test Home Page Title FAILED *********")
            self.driver.close()
            assert False


    def test_login(self, setup):
        self.logger.info("********* Started Login Test *********")
        self.driver = setup
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.baseUrl)
        self.loginPage = LoginPage(self.driver)  ## instance of login page
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        time.sleep(1)
        actual_title = self.driver.title
        
        if actual_title == "Dashboard / nopCommerce administration":
            # I've noticed a modal that appear and obscure the logout link  
            # So I've checked its presence and click it if present
            modalBtn = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[1]/div/div[3]/span")
            
            if modalBtn.is_displayed():
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login_after_logout.png")
                modalBtn.click()
                # Here i'm waiting for the modal to disappear before clicking the logout link
                wait.until(
                    EC.invisibility_of_element((By.CLASS_NAME, "modal-backdrop"))
                )
                
            self.loginPage.clickLogout()  
            self.logger.info("********* Login Test PASSED *********")
            self.driver.close()    
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("********* Login Test FAILED *********")
            self.driver.close()
            assert False
