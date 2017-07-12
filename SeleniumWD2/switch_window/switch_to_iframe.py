from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()

    def test1(self):
        driver = self.driver
        baseUrl = "https://letskodeit.teachable.com"
        driver.get(baseUrl + "/p/practice")

        element = driver.find_element(By.XPATH, "//legend[contains(.,'iFrame Example')]")
        #scrolling to iframe
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)

        # switch to frame
        driver.switch_to.frame("iframe-name") # another way switch_to.frame(0)
        # make some actions in frame
        driver.find_element(By.XPATH, "//input[@id='search-courses']").send_keys("java\n")
        time.sleep(2)
        # switch back
        driver.switch_to.default_content()

        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("java2222")
        time.sleep(2)
        driver.quit()


ff = SwitchToFrame()
ff.test1()