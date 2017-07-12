from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class FindElemetBy_XPAth_CSS():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        # exercise №1: Find prise of course "Python programming language"
        elementByXPath = driver.find_element_by_xpath(".//*[@id='product']//td[contains(text(),'Python')]/following-sibling::td")
        if elementByXPath is not None:
            print("Python Course price = {}".format(elementByXPath.text))

        # exercise №2: Find telefhone number of user Lucie Land
        driver.get("https://dhtmlx.com/docs/products/dhtmlxGrid/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'gridbox')]//td[text()='Lucie Land']")))
        elementByXPath = driver.find_element_by_xpath("//div[contains(@class,'gridbox')]//td[text()='Lucie Land']//following-sibling::td[3]")
        if elementByXPath is not None:
            print("Lucie Land number = {}".format(elementByXPath.text))

        driver.close()

ff = FindElemetBy_XPAth_CSS()
ff.test()