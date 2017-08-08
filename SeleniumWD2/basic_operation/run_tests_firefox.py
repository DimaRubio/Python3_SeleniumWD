from selenium import webdriver

class RunFFTests():

    #ranning simple test on Firefox
    def test(self):
        driver = webdriver.Firefox()
        driver.get("https://ru.stackoverflow.com/")

ff = RunFFTests()
ff.test()