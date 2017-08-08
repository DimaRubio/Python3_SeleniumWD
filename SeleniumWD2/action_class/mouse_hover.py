from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from  selenium.webdriver import ActionChains

class Test():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    action = ActionChains(driver)
    baseUrl = "https://letskodeit.teachable.com"
    driver.get(baseUrl + "/p/practice")

    def baseTest(self):
        driver = self.driver
        self.test1(driver)
        self.test2(driver)
        driver.quit()

    #test shows how move cursor on element
    def test1(self, driver):
        self.scroll(driver)
        element = driver.find_element_by_id("mousehover")
        self.action.move_to_element(element).perform()
        driver.find_element(By.XPATH,"//a[contains(.,'Top')]").click()

    # test shows how move cursor and click on element
    def test2(self, driver):
        self.scroll(driver)
        element = driver.find_element_by_id("mousehover")
        self.action.move_to_element(element).perform()
        elementClick = driver.find_element(By.XPATH, "//a[contains(.,'Reload')]")
        self.action.move_to_element(elementClick).click().perform()
        time.sleep(2)

    def scroll(self, driver):
        element = driver.find_element(By.XPATH, "//legend[contains(.,'Mouse Hover Example')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)


ff = Test()
ff.baseTest()
