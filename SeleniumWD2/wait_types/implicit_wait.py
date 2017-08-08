from selenium import webdriver

class Implicit_Wait():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        #set implicitly time wait equal 6 seconds
        driver.implicitly_wait(6)
        driver.maximize_window()

        driver.get(baseUrl)

        loginItem = driver.find_element_by_css_selector("a[href='/sign_in']")
        loginItem.click()

        emeil_field = driver.find_element_by_css_selector("#user_email")
        emeil_field.send_keys("abcdefg")

        password_field = driver.find_element_by_id("user_password")
        password_field.send_keys("123456")

        driver.quit()

ff = Implicit_Wait()
ff.test()