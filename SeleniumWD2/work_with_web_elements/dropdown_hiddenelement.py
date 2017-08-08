from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DropDownHidden():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(6)
        driver.maximize_window()
        driver.get(baseUrl + "/pages/practice")

        # exercice reperesent how work with dropdown
        element = driver.find_element_by_id("carselect")
        dropDown = Select(element)
        dropDown.select_by_index(1)
        time.sleep(2)
        dropDown.select_by_value("honda")
        time.sleep(2)
        dropDown.select_by_visible_text("Benz")
        time.sleep(2)

        # exercices below reperesent difference between displayed status and enabled stutus of element
        element = driver.find_element_by_id("displayed-text")
        print("block is displayed? "+ str(element.is_displayed()))
        print("block is displayed? " + str(element.is_enabled()))
        time.sleep(2)

        driver.find_element_by_id("hide-textbox").click()
        print("block is displayed? " + str(element.is_displayed()))
        print("block is displayed? " + str(element.is_enabled()))

        driver.get("https://www.expedia.com/")
        time.sleep(4)
        driver.find_element_by_id("tab-flight-tab-hp").click()
        time.sleep(2)
        drpdwnElement = driver.find_element_by_id("flight-age-select-1-hp-flight")
        print("Element visible? " + str(drpdwnElement.is_displayed()))
        print("Element visible? " + str(drpdwnElement.is_enabled()))

        driver.quit()

ff = DropDownHidden()
ff.test()