import os
from traceback import print_stack

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import AutoTestFramework.utilities.custom_logger as cl
import logging

class SeleniumDriver():

    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("locator type \"{0}\" not supported".format(locatorType))
        return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.1):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting element with locator \"{0}\" not found on the web page during {1} sec. Details: {1}".format(locator, str(timeout)))
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print("success")
        except TimeoutException as ex:
            print("Element with locator \"{0}\" not found on the web page during 20 sec. Details: {1}".format(locator, str(ex)))
            print_stack()
        return element

    def getTitle(self):
        return self.driver.title

    def screenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception occurred when taking screenshot")
            print_stack()


