from selenium import webdriver

class Browser_Interaction():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()

        driver.maximize_window()

        #open page by "https://letskodeit.teachable.com/p/practice"
        driver.get(baseUrl + "/p/practice")
        print("url = {0}".format(driver.current_url))

        #get title of page
        title = driver.title
        print("Title is: " + title)

        # get current url
        url = driver.current_url
        print("Current URL is: " + url)

        #refresh page
        driver.refresh()

        # another way to refresh page
        driver.get(driver.current_url)

        driver.get(baseUrl+"/secure/42299/users/sign_in?reset_purchase_session=1")
        print("Current URL is: " + driver.current_url)

        #go back by one page on the browser history
        driver.back()
        print("Go back to "+ driver.current_url)

        #go forward by one page on the browser history
        driver.forward()
        print("Go forward to " + driver.current_url)

        # Get Page Source
        pageSource = driver.page_source
        print(pageSource[0:150])

        driver.quit()

ff = Browser_Interaction()
ff.test()