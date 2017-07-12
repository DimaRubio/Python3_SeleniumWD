from selenium import webdriver

class FindElemetBy_CSS_Advance():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        # finding element using css selector by tag with particular class which ending displayed-class'
        elementByCSS = driver.find_element_by_css_selector("input[class$='displayed-class']")        # 1 matching, because ending 'displayed-class'
        if elementByCSS is not None:
            print("Represents the ending text")

        # finding element using css selector by tag with particular class which starting from text 'displayed-class'
        try:
            elementByCSS = driver.find_element_by_css_selector("input[class^='displayed-class']")    # no matching
            if elementByCSS is not None:
                print("Represents the starting text")
        except:
            print("no matching")

        # finding element using css selector by tag with particular class which starting from text 'displayed-class'
        elementByCSS = driver.find_element_by_css_selector("input[class^='inputs']")                 # 2 matching, because starting from "input"
        if elementByCSS is not None:
            print("Represents the starting text ")

        # finding element using css selector by tag with attribute "placeholder" which contains text 'Your'
        elementByCSS = driver.find_element_by_css_selector("input[placeholder*='Your']")   # 1 matching, because contains  "Your" in center of pleceholder
        if elementByCSS is not None:
            print("Represents the text contained ")

        print("*" * 10, "CSS_Advance_Finding_Child", "*" * 10)

        #example which represent how find all element on particular level of DOM
        listElementByCSS = driver.find_elements_by_css_selector("#radio-btn-example>fieldset>legend ~ label")   # find all label tags  down from legend tag  on the same level
        if listElementByCSS is not None:
            print("all label tags  down from legend tag  on the same level  ")
            for item in listElementByCSS:
                print(item.text)

        # example which represent how find first element on particular level of DOM
        listElementByCSS = driver.find_elements_by_css_selector("#radio-btn-example>fieldset>legend + label")   # find first label tags  down from legend tag on the same level
        if listElementByCSS is not None:
            print("first label tags  down from legend tag on the same level")
            for item in listElementByCSS:
                print(item.text)

        # example which represent how find particular child tag
        listElementByCSS = driver.find_elements_by_css_selector("#radio-btn-example>fieldset>:nth-child(3)")
        if listElementByCSS is not None:
            print("find third child tag")
            for item in listElementByCSS:
                print(item.text)

        driver.close()

if __name__ =="__main__":
    ff = FindElemetBy_CSS_Advance()
    ff.test()