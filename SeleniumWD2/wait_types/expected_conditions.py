from selenium import webdriver
from selenium.webdriver.common.by import By
from SeleniumWD2.wait_types.explicit_wait_wrapper import ExplicitWaitWrapper

class Expected_Conditions():

    def test(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(baseUrl)

        # search flight from Kiev to Minsk
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("KBP")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("MSQ")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("08/20/2017")
        driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("08/26/2017")
        driver.find_element(By.XPATH, "//*[@id='section-flight-tab-hp']//span[text()='Search']").click()

        wait = ExplicitWaitWrapper(driver)
        # waiting 20 seconds while searching to be completed
        element = wait.waitForElementById("Nonstop-stop-flights-checkbox")
        element.click()

        driver.quit()


ff = Expected_Conditions()
ff.test()