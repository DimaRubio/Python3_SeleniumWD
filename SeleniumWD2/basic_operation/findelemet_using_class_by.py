from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElemet_Class_By():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        # example which represent how find element by class name using built-in methods class By
        elementByClass = driver.find_element(By.CLASS_NAME, "displayed-class")
        if elementByClass is not None:
            print("element by Class is found")

        #  example which represent how find element by css selector using built-in methods class By
        elementByCSS = driver.find_element(By.CSS_SELECTOR,".displayed-class")
        if elementByCSS is not None:
            print("same element by CSS is found")

        #  example which represent how find element by tag using built-in methods class By
        elementByTag = driver.find_element(By.TAG_NAME, "h1")
        if elementByTag is not None:
            print("same element by Tag is found: {}".format(elementByTag.text) )

        driver.close()

ff =  FindElemet_Class_By()
ff.test()