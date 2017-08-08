from selenium import webdriver

class FindElemetBy_Class_And_Tag_Name():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        # example which represent how find element by particular class name
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        if elementByClassName is not None:
            print("element by Class Name is found")

        # finding same element from the previous example using css selector by CSS-class
        elementByCSS = driver.find_element_by_css_selector(".displayed-class")
        if elementByCSS is not None:
            print("same element by CSS selector is found")

        # example which represent how find element by tag
        elementByTagName = driver.find_element_by_tag_name("h1")
        if elementByTagName is not None:
            print("same element by Tag Name is found: {}".format(elementByTagName.text) )

        driver.close()

if __name__ =="__main__":
    ff = FindElemetBy_Class_And_Tag_Name()
    ff.test()