from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class FindElemetBy_XPAth_CSS():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        # finding element using xpath selector by input tag  which contains particular id
        elementByXPath = driver.find_element_by_xpath("//input[@id='name']")
        if elementByXPath is not None:
            print("element by XPath is found")

        # finding element using xpath selector by legend tag which with text
        elementByXPath = driver.find_element_by_xpath("//legend[text()='Radio Button Example']")
        if elementByXPath is not None:
            print("using text to build XPath")

        # finding element using xpath selector by legend tag which contains particular text
        elementByXPath = driver.find_element_by_xpath("//legend[contains(text(),'Button Example')]")
        if elementByXPath is not None:
            print("using \"contains\" keyword and text to build XPath")

        # finding element using xpath selector by button tag which contains several particular attribute
        elementByXPath = driver.find_element_by_xpath("//button[contains(@class,'btn-style') and contains(@onclick,'openWindow')]")
        if elementByXPath is not None:
            print("using \"contains\" keyword and class css to build XPath")

        # finding element using xpath selector by link tag that contains css class which starting from text 'navbar-l'
        elementByXPath = driver.find_element_by_xpath("//a[starts-with(@class, 'navbar-l')]")
        if elementByXPath is not None:
            print("using \"starts-with\" keyword and class css to build XPath")

        # example which represent how find element following from current on the same level
        print("*"*10,"Advance Xpath")
        elementByXPath = driver.find_element_by_xpath(".//*[@id='product']//td[contains(text(),'Python')]/following-sibling::td")
        if elementByXPath is not None:
            print("Python Course price = {}".format(elementByXPath.text))

        # example which represent how find third element following from current on the same level
        driver.get("https://dhtmlx.com/docs/products/dhtmlxGrid/")
        #time.sleep(5)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'gridbox')]//td[text()='Lucie Land']")))
        elementByXPath = driver.find_element_by_xpath("//div[contains(@class,'gridbox')]//td[text()='Lucie Land']//following-sibling::td[3]")
        if elementByXPath is not None:
            print("Lucie Land number = {}".format(elementByXPath.text))

        driver.close()

if __name__ =="__main__":
    ff = FindElemetBy_XPAth_CSS()
    ff.test()