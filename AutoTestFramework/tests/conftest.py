import os
from traceback import print_stack
import pytest
import time
from AutoTestFramework.base.webdriver_factory import WebDriverFactory
from AutoTestFramework.pages.login_page import LoginPage
from AutoTestFramework.utilities.teststatus import TestStatus


@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getDriverInstance()

    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")
    testStatus = TestStatus(driver)
    # add `driver` and 'login page' as attribute to the test class
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.lp = lp
        request.cls.testStatus = testStatus

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")