from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Take_Screnshot():

    #test shows how take screenshot if test was failed
    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(6)
        driver.maximize_window()

        driver.get(baseUrl)

        loginItem = driver.find_element_by_css_selector("a[href='/sign_in']")
        loginItem.click()

        emeil_field = driver.find_element_by_css_selector("#user_email")
        #enter wrong email
        emeil_field.send_keys("abcdefg")

        password_field = driver.find_element_by_id("user_password")
        password_field.send_keys("123456")
        driver.find_element(By.XPATH, "//input[@name='commit']").click()
        self.takeScreenshot(driver)

        time.sleep(2)
        driver.quit()

    def takeScreenshot(self, driver):

        fileName = str(round(time.time() * 1000)) + ".png"

        screenshotDirectory = "/home/dmytro.bolyachin/TestDir/Python/dmytro.bolyachin-Selenium_webdriver_with_Python3/SeleniumWD2/sw_advanced/"
        pathToFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(pathToFile)
            print("Screenshot saved to directory: " + pathToFile)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Take_Screnshot()
ff.test()