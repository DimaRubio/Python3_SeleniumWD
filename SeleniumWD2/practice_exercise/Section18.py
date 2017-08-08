from selenium import webdriver
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AirbnbTest():

    def test(self):
        baseUrl = "https://www.airbnb.com"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.implicitly_wait(8)

        #type country to visit
        driver.find_element(By.XPATH,"//input[@id='GeocompleteController-via-SearchBarLarge-via-HeroController']").send_keys("philippines")
        #click on search button
        driver.find_element(By.CSS_SELECTOR, "button[class*='search']").click()

        wait = WebDriverWait(driver, 20, poll_frequency=2)
        # wait until calendar is present
        elementStartDate = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Check In']")))
        #type date
        elementStartDate.send_keys("Aug 2")
        driver.find_element(By.XPATH,"//input[@id='endDate']").send_keys("Aug 3")

        driver.quit()

ff = AirbnbTest()
ff.test()