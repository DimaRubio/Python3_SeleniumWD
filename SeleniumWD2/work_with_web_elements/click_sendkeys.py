from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Click_Type():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(6)
        driver.maximize_window()

        driver.get(baseUrl + "/pages/practice")
        print("url = {0}".format(driver.current_url))

        title = driver.title
        print("Title is: " + title)

        #click on login icon
        loginItem = driver.find_element_by_css_selector("a[href='/sign_in']")
        loginItem.click()

        #type text to email field
        emeil_field = driver.find_element_by_css_selector("#user_email")
        emeil_field.send_keys("abcdefg")

        # type text to password field
        password_field = driver.find_element_by_id("user_password")
        password_field.send_keys("123456")

        #clear email field
        emeil_field.clear()

        time.sleep(2)

        emeil_field.send_keys("test222")

        time.sleep(2)

        driver.quit()

ff = Click_Type()
ff.test()