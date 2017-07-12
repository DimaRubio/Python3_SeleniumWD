from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        #  examples below represent how set upp list of elemets and count amount, using different selectors
        listElementByClass = driver.find_elements(By.CLASS_NAME, "displayed-class")
        if listElementByClass is not None:
            length = len(listElementByClass)
            print("Amount elements By.CLASS_NAME: {}".format(str(length)))

        listElementByCSS = driver.find_elements_by_css_selector(".inputs")
        if listElementByCSS is not None:
            length = len(listElementByCSS)
            print("Amount elements by CSS:{}".format(str(length)))

        listElementByTag = driver.find_elements(By.TAG_NAME, "tr")
        if listElementByTag is not None:
            for item in listElementByTag:
                print(item.text)

        driver.close()

ff =  ListOfElements()
ff.test()