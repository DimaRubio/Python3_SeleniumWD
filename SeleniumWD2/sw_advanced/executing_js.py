from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Execute_JS():

    #test shows how find element using js
    def test1(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(6)
        driver.maximize_window()

        driver.execute_script("window.location = 'https://letskodeit.teachable.com';")
        loginItem = driver.find_element_by_css_selector("a[href='/sign_in']")
        loginItem.click()

        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.ID, "user_email")))

        #find element using js
        emeil_field = driver.execute_script("return document.getElementById('user_email');")
        emeil_field.send_keys("abcdefg")


        password_field = driver.find_element_by_id("user_password")
        password_field.send_keys("123456")
        driver.find_element(By.XPATH, "//input[@name='commit']").click()

        #get Height and Width of page
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height = {} ".format(str(height)))
        print("Width = {} ".format(str(width)))

        time.sleep(2)
        driver.quit()

    # test shows how scrolling page using js different ways
    def test2(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(6)
        driver.maximize_window()

        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")

        #scrolling down using js
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

        # scrolling up using js
        driver.execute_script("window.scrollBy(0, -500);")
        time.sleep(4)

        # scrolling to webelement using js
        element = driver.find_element(By.XPATH, "//legend[contains(.,'iFrame Example')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)

        # scrolling up using js
        driver.execute_script("window.scrollBy(0, -500);")
        time.sleep(4)

        # scrolling to webelement using location
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))

        time.sleep(2)
        driver.quit()


ff = Execute_JS()
ff.test1()
ff.test2()