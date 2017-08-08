from selenium.webdriver.common.by import By
from AutoTestFramework.base.selenium_driver import SeleniumDriver
from selenium import webdriver
from AutoTestFramework.pages.base_page import BasePage
from AutoTestFramework.pages.navigate_bar import NavigateBar

class LoginPage(NavigateBar):

    # Locators
    _login_link = "//a[contains(@href,'/sign_in')]"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "//input[@value='Log In']"
    _erMsg = ".alert.alert-danger"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getLoginItem(self):
        return self.driver.find_element(By.XPATH, self._login_link)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def getErMsg(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._erMsg)

    def login(self, email, password):
        self.getLoginItem().click()
        self.getEmailField().send_keys(email)
        self.getPasswordField().send_keys(password)
        self.getLoginButton().click()



