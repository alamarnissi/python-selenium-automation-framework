
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        username_field = self.driver.find_element(By.ID, self.textbox_username_id)
        username_field.clear()
        username_field.send_keys(username)

    def setPassword(self, password):
        password_field = self.driver.find_element(By.ID, self.textbox_password_id)
        password_field.clear()
        password_field.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()