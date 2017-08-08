from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from  selenium.webdriver import ActionChains

class Test():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    action = ActionChains(driver)
    baseUrl = "https://jqueryui.com/slider/"
    driver.get(baseUrl)

    def baseTest(self):
        driver = self.driver
        self.test1(driver)
        driver.quit()

    def test1(self, driver):
        driver.switch_to.frame(0)
        element = driver.find_element_by_css_selector(".ui-slider-handle")
        #horizontally move the slider to 400 pixels
        self.action.drag_and_drop_by_offset(element, 400, 0).perform()
        time.sleep(4)
        #switch back to page content
        driver.switch_to.default_content()
        print("Success")

ff = Test()
ff.baseTest()
