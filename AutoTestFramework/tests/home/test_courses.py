import os
import unittest
from AutoTestFramework.pages.courses_page import CoursesPage
from AutoTestFramework.pages.checkout_page import CheckOutPage
import pytest
from AutoTestFramework.utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
from AutoTestFramework.utilities.recognize_csv import recognizeCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class CoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        #Create Page
        self.coursePage = CoursesPage(self.driver)
        self.checkOutPage = CheckOutPage(self.driver)
        self.testStatus = TestStatus(self.driver)

    def setUp(self):
        self.driver.get("https://letskodeit.teachable.com/courses")

    @pytest.mark.run(order=1)
    #Get data for tests from file /resourses/testdata.csv
    @data(*recognizeCSVData(os.getcwd()+"/resourses/testdata.csv"))
    @unpack
    def	test_invalidEnrollment(self, course, number, exp, cvv, country):
        self.coursePage.findCourse(course)
        self.coursePage.getEnrollButton().click()
        self.checkOutPage.enrollCourse(number, exp, cvv, country)
        self.assertIsNotNone(self.checkOutPage.getErMsg())
        print("success")