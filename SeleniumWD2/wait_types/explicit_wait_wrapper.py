from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
from selenium.webdriver.common.by import By
class ExplicitWaitWrapper:

    def __init__(self, driver):
        self.driver = driver

    def waitForElementById(self, locator, timeout=20, pollFrequency = 0.5):
        element = None
        try:
            print("Waiting " + str(timeout) + " seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency, ignored_exceptions=[NoSuchElementException,
                                                                                   ElementNotVisibleException,
                                                                                   ElementNotSelectableException])

            element = wait.until(EC.element_to_be_clickable((By.ID, locator)))
            print("success")
        except:
            print("Element not found on the web page")
            print_stack()

        return element