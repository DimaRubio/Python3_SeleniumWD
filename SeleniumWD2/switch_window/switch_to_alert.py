from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToAlert():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()

    def test1(self):
        driver = self.driver
        baseUrl = "https://letskodeit.teachable.com"
        driver.get(baseUrl + "/p/practice")

        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Dima")
        driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
        time.sleep(2)
        #click "Ok" button in allert
        driver.switch_to.alert.accept()

        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Dima")
        driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
        time.sleep(2)
        # click "Cancel" button in allert
        driver.switch_to.alert.dismiss()

        time.sleep(2)
        driver.quit()


ff = SwitchToAlert()
ff.test1()