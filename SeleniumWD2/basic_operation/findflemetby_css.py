from selenium import webdriver

class FindElemetBy_CSS():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        print("*"*10,"Css-selectors","*"*10)

        # finding element using css selector by tag which contains particular id
        elementByCSS = driver.find_element_by_css_selector("input[id='name']")  # command will find tag in DOM <input id="name" class="inputs" name="enter-name" placeholder="Enter Your Name" type="text"/>
        if elementByCSS is not None:
            print("same element using CSS-selector tag[attribute = 'value']")

        # finding element using css selector by id
        elementByCSS = driver.find_element_by_css_selector("#name") #command will find tag in DOM <input id="name" class="inputs" name="enter-name" placeholder="Enter Your Name" type="text"/>
        if elementByCSS is not None:
            print("same element using CSS-selector by id is found")

        # finding element using css selector by CSS-class
        elementByCSS = driver.find_element_by_css_selector(".displayed-class")        #command will find tag with attribute class="inputs displayed-class"
        if elementByCSS is not None:
            print("contains one of many CSS-class ")

        # finding element using css selector which contains several css-classes
        elementByCSS = driver.find_element_by_css_selector(".inputs.displayed-class") #command will find tag with attribute  class="inputs displayed-class"
        if elementByCSS is not None:
            print("contains both CSS-class")

        # finding element using css selector which contains css-class and id
        elementByCSS = driver.find_element_by_css_selector(".inputs#name")  #command will find tag in DOM <input id="name" class="inputs" name="enter-name" placeholder="Enter Your Name" type="text"/>
        if elementByCSS is not None:
            print("mixed selector contains CSS-class and id")

        # finding element using css selector which contains CSS-class of particular tag
        elementByCSS = driver.find_element_by_css_selector("input.displayed-class")  #command will find tag in DOM <input id="displayed-text" class="inputs displayed-class" name="show-hide" placeholder="Hide/Show Example" type="text"/>
        if elementByCSS is not None:
            print("mixed selector contains CSS-class of particular tag")

        driver.close()

if __name__ =="__main__":
    ff = FindElemetBy_CSS()
    ff.test()