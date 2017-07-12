from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWinow():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()

    def test1(self):
        driver = self.driver
        baseUrl = "https://letskodeit.teachable.com"
        driver.get(baseUrl + "/p/practice")
        #get number of current window
        parentWindow = driver.current_window_handle

        driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
        # switch to new window
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

        #make some actions in new window
        driver.find_element(By.XPATH, "//input[@id='search-courses']").send_keys("java")
        time.sleep(2)
        driver.close()
        #switch back
        driver.switch_to.window(parentWindow)

        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("java2222")
        time.sleep(2)
        driver.quit()


ff = SwitchToWinow()
ff.test1()

