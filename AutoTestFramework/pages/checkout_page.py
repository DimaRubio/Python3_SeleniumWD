from selenium.webdriver.common.by import By
from AutoTestFramework.pages.base_page import BasePage
from selenium.webdriver.support.select import Select

class CheckOutPage(BasePage):

    # Locators
    _cc_number_field = "//input[@id='cc_field']"
    _cc_exp_field = "//input[@id='cc-exp']"
    _cc_cvc_field = "//input[@id='cc_cvc']"
    _cc_country_select = "//select[@id='country-select-inside']"
    _cc_verify_button ="//button[@id='verify_cc_btn']"
    _erMsg = ".payment-errors.undefined"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enrollCourse(self, number="", exp="", cvv="", country="RU"):
        self.scrollPage("down")

        self.getCCNumberField().send_keys(number)
        self.getCCExpField().send_keys(exp)
        self.getCCCVCField().send_keys(cvv)
        element = self.getCCCountrySelect()
        sel = Select(element)
        sel.select_by_value(country)
        self.getCCVerifeButton().click()

    def getCCNumberField(self):
        return self.driver.find_element(By.XPATH, self._cc_number_field)

    def getCCExpField(self):
        return self.driver.find_element(By.XPATH, self._cc_exp_field)

    def getCCCVCField(self):
        return self.driver.find_element(By.XPATH, self._cc_cvc_field)

    def getCCCountrySelect(self):
        return self.driver.find_element(By.XPATH, self._cc_country_select)

    def getCCVerifeButton(self):
        return self.driver.find_element(By.XPATH, self._cc_verify_button)

    def getErMsg(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._erMsg)




