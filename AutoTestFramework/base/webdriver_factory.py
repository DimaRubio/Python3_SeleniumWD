from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getDriverInstance(self):
        baseURL = "https://letskodeit.teachable.com/"
        if self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)
        return driver


