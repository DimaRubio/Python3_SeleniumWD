import AutoTestFramework.utilities.custom_logger as cl
import logging
import inspect
from AutoTestFramework.base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.result_List = []

    def setResult(self, result, resultMessage):
        reason = ""
        try:
            if result is not None:
                if result:
                    self.result_List.append("PASS")
                    reason = resultMessage + " SUCCESSFUL"

                else:
                    self.result_List.append("FAIL")
                    reason = resultMessage + " FAILED"
                    # Take screenshot if assert failed
                    self.screenShot(reason)
            else:
                self.result_List.append("FAIL")
                reason = resultMessage + " FAILED"
                self.screenShot(reason)
        except:
            self.result_List.append("FAIL")
            reason = "Exception Occurred"
            self.screenShot(reason)
        return reason

    def markAssert(self, result, resultMessage):
        testName = inspect.stack()[1][3]
        reason = self.setResult(result, resultMessage)
        if "FAIL" in self.result_List:
            self.log.error("Test \"{0}\" - FAILED :: Reason - {1}".format(testName, reason))
        else:
            self.log.info("Test \"{0}\" - PASSED :: Reason - {1}".format(testName, reason))

    def markAssertFinal(self, result, resultMessage):
        testName = inspect.stack()[1][3]
        reason = self.setResult(result, resultMessage)

        if "FAIL" in self.result_List:
            self.log.error("Test \"{0}\" - FAILED :: Reason - {1}".format(testName, reason))
            self.result_List.clear()
            assert True == False
        else:
            self.log.info("Test \"{0}\" - PASSED :: Reason - {1}".format(testName, reason))
            self.result_List.clear()
            assert True == True