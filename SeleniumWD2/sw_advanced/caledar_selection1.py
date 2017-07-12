from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class Expected_Conditions():

    def test1(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("KBP")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("MSQ")

        # select departing date
        driver.find_element(By.ID, "flight-departing-hp-flight").click()
        driver.find_element(By.XPATH, ".//*[@class='datepicker-cal-month'][position()=2]//button[text()=25]").click()

        # select returning date and search
        driver.find_element(By.ID, "flight-returning-hp-flight").click()
        driver.find_element(By.XPATH, ".//*[@class='datepicker-cal-month'][position()=2]//button[text()=28]").click()
        driver.find_element(By.XPATH, "//*[@id='section-flight-tab-hp']//span[text()='Search']").click()

        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                               ElementNotVisibleException,
                                                                               ElementNotSelectableException])
        # waiting 20 seconds while searching to be completed
        element = wait.until(EC.element_to_be_clickable((By.ID, "Nonstop-stop-flights-checkbox")))
        element.click()

        time.sleep(2)
        print("success")
        driver.quit()

    def test2(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(baseUrl)

        # search flight from Kiev to Minsk
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("KBP")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("MSQ")

        #click on departing datepicker
        driver.find_element(By.ID, "flight-departing-hp-flight").click()
        #get all active dates in calendar
        activeDateList = driver.find_elements(By.XPATH,".//*[@class='datepicker-cal-month'][position()=1]//button[contains(@data-day,.)]")
        for date in activeDateList:
            #Click on 28 date of current month
            if date.text == "28":
                date.click()
                break

        # select returning date and search
        driver.find_element(By.ID, "flight-returning-hp-flight").click()
        driver.find_element(By.XPATH, ".//*[@class='datepicker-cal-month'][position()=2]//button[text()=28]").click()
        driver.find_element(By.XPATH, "//*[@id='section-flight-tab-hp']//span[text()='Search']").click()

        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                               ElementNotVisibleException,
                                                                               ElementNotSelectableException])
        # waiting 20 seconds while searching to be completed
        element = wait.until(EC.element_to_be_clickable((By.ID, "Nonstop-stop-flights-checkbox")))
        element.click()

        time.sleep(2)
        print("success")
        driver.quit()


ff = Expected_Conditions()
ff.test1()
ff.test2()