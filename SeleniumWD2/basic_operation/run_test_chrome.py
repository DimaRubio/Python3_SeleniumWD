from selenium import webdriver
import os

class RunChromeTests():

    # ranning simple test on Chrome
    def test(self):
        # driverLocation = "/home/dmytro.bolyachin/Programs/SeleniumDrivers"
        driver = webdriver.Chrome()
        driver.get("https://ru.stackoverflow.com/")

ch = RunChromeTests()
ch.test()