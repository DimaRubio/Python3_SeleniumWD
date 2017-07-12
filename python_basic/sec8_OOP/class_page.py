class BasePage:

    def __init__(self):
        print("You created BasePage")

    def elementIsPresent(self):
        print("element is present on the BasePage")

    def refreshPage(self):
        print("refresh the base page")

class LoginPage(BasePage):

    def __init__(self):
        BasePage.__init__(self)
        print("You created LoginPage")

    def elementIsPresent(self):
        super().elementIsPresent()
        print("element is present on the LoginPage")

    def clickLoginItem(self):
        print("click on Login Item")

if __name__ == "__main__":
    b = BasePage()
    b.elementIsPresent()
    b.refreshPage()
    # b.clickLoginItem      #not supported method for instance of base class

    l = LoginPage()
    l.elementIsPresent()
    l.refreshPage()
    l.clickLoginItem()