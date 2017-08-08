from selenium.webdriver.common.by import By
from AutoTestFramework.base.selenium_driver import SeleniumDriver
from selenium import webdriver
from AutoTestFramework.pages.base_page import BasePage

class CoursesPage(BasePage):

    # Locators
    _avatar = ".gravatar"
    _search_field = "//input[@id='search-courses']"
    _search_button = "//button[@id='search-course-button']"
    _course_block = "//div[contains(text(),'{}') and contains(@class,'course-listing-title')]"
    _enroll_course_button = "//button[@id='enroll-button-top']"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getAvatar(self):
        return  self.driver.find_element(By.CSS_SELECTOR, self._avatar)

    def getSearchField(self):
        return self.driver.find_element(By.XPATH, self._search_field)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self._search_button)

    def findCourse(self, query):
        self.getSearchField().send_keys(query)
        self.getSearchButton().click()
        self.selectNeedfullCourse(query)

    def selectNeedfullCourse(self, query):
        locator = self._course_block
        self.driver.find_element(By.XPATH, locator.format(query)).click()

    def getEnrollButton(self):
        return self.driver.find_element(By.XPATH, self._enroll_course_button)







