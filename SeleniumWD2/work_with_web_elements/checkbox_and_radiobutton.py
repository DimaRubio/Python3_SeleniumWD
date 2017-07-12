# work with checkbox and radiobutton

from selenium import webdriver
from selenium.webdriver.common.by import By

class CheckboxRadiobutton():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(6)
        driver.maximize_window()

        driver.get(baseUrl + "/pages/practice")
        print("url = {0}".format(driver.current_url))

        #Click on radio button
        radioBenz = driver.find_element_by_id("benzradio")
        radioBenz.click()
        print("benz radio button is selected?" + str(radioBenz.is_selected()))

        # Select benz checkbox
        checkBenz = driver.find_element_by_id("benzcheck")
        checkBenz.click()
        print("benz checkbox is selected? " + str(checkBenz.is_selected()))

        # Unselect benz checkbox
        checkBenz.click()
        print("benz checkbox is selected? " + str(checkBenz.is_selected()))

        #takes all checkbox
        listOfCheckBox = driver.find_elements(By.XPATH,".//input[@type='checkbox' and @name='cars']/parent::label")
        for item in listOfCheckBox:
            print("Value = {}".format(item.text))

        driver.quit()

ff = CheckboxRadiobutton()
ff.test()