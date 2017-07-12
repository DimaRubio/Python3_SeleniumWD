from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from  selenium.webdriver import ActionChains

class Test():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    action = ActionChains(driver)
    baseUrl = "https://jqueryui.com/droppable/"
    driver.get(baseUrl)

    def baseTest(self):
        driver = self.driver
        self.test1(driver)
        driver.quit()

    def test1(self, driver):
        driver.switch_to.frame(0)
        element = driver.find_element(By.ID, "draggable")
        dropElement = driver.find_element(By.ID, "droppable")
        time.sleep(2)
        self.action.drag_and_drop(element, dropElement).perform()
        #Another way is use comand below:
        #self.action.click_and_hold(element).move_to_element(dropElement).release().perform()
        time.sleep(2)
        driver.switch_to.default_content()
        print("Success")

ff = Test()
ff.baseTest()
