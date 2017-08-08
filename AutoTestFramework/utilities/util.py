import time
import traceback
import random, string
import AutoTestFramework.utilities.custom_logger as cl
import logging

class Util:

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):

        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def verifyTextContains(self, actualText, expectedText):

        if expectedText.lower() in actualText.lower():
            return True
        else:
            return False

    def verifyTextMatch(self, actualText, expectedText):

        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False