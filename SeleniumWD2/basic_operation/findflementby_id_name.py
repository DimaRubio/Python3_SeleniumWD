from selenium import webdriver

class FindElemetBy_Id_Name():

    baseUrl = "https://letskodeit.teachable.com/pages/practice"
    driver = webdriver.Firefox()
    driver.get(baseUrl)

    # finding element by ID
    def test_find_element_by_id(self, id):

        elementById = self.driver.find_element_by_id(id)
        if elementById is not None:
            print("element by Id is found")

    # finding element by name
    def test_find_element_by_name(self, name):
        elementByName = self.driver.find_element_by_name(name)
        if elementByName is not None:
            print("same element by Name is found")
        self.driver.close()

if __name__ =="__main__":
    ff = FindElemetBy_Id_Name()
    ff.test_find_element_by_id("name")
    ff.test_find_element_by_name("enter-name")
