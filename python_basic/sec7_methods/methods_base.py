class WebDriver():

    def setUrl(self, baseUrl ="https://letskodeit.teachable.com", url=""):
        self.url = baseUrl + url

    def getUrl(self):
        return self.url

    def assertUrl(self,url):
        currentUrl = self.getUrl()
        return True if currentUrl == url else False

    def containsUrl(self,url):
        currentUrl = self.getUrl()
        return True if url in currentUrl else False

if __name__ == "__main__":
    driver = WebDriver()
    driver.setUrl(url="/login")
    print(driver.getUrl())
    print(driver.assertUrl("https://letskodeit.teachable.com/"))
    print(driver.containsUrl("https://letskodeit.teachable.com/"))


