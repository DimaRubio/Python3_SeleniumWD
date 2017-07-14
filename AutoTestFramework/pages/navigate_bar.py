from selenium.webdriver.common.by import By
from AutoTestFramework.pages.base_page import BasePage
import time

class NavigateBar(BasePage):

    # Locators
    _avatar = ".gravatar"
    _logout_item = "//div[@id='navbar']//a[@href='/sign_out']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getAvatar(self):
        return  self.driver.find_element(By.CSS_SELECTOR, self._avatar)

    def getLogoutItem(self):
        return  self.driver.find_element(By.XPATH, self._logout_item)

    def logout(self):
        self.getAvatar().click()
        time.sleep(2)
        self.getLogoutItem().click()

