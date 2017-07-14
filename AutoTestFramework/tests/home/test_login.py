import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    #test for authorisation with valid login
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        self.testStatus.markAssertFinal(self.lp.titleContainsText("Let's Kode"), "Title Verified")
        self.assertIsNotNone(self.lp.getAvatar())
        print("success")

    #test for authorisation with invalid login
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        #logout from the site because 'oneTimeSetUp' fixture consist login
        self.lp.logout()
        self.lp.login("", "abcabc")
        self.testStatus.markAssert(self.lp.titleContainsText("Let's Kode"), "Title Verified")
        self.testStatus.markAssertFinal(self.lp.elementPresent(self.lp.getErMsg()), "Msg doesn't displayed")
        print("success")
