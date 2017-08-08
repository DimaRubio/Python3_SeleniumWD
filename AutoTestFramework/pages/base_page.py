from AutoTestFramework.base.selenium_driver import SeleniumDriver
from traceback import print_stack
from AutoTestFramework.utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    def titleContainsText(self, titleToVerify):
        try:
            actual_title = self.getTitle()
            return self.util.verifyTextContains(actual_title, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def elementPresent(self, element):
        if element is not None:
            return True
        else:
            return False

    def scrollPage(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")