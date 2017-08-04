#For run this test case type to command line "py.test -v -s pytest_2/test_class.py --browser firefox" in project directory
#For run this test case with html report type to command line "py.test -v -s test_class.py --browser firefox --html=report.html"
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp") #fixtures applied for each test method in class
class TestClass1():

    # common fixtures for each test in class
    @pytest.fixture(autouse=True)               #argument "autouse=True" has the same meaning as @pytest.mark.usefixtures("Some_Fixtures")
    def setUpInClass(self, oneTimeSetUp):
        #get value from fixture oneTimeSetUp
        self.value_from_fixture = self.value

    def test_login(self):
        assert 10 == self.value_from_fixture
        print("Body Test Login")

    def test_profile(self):
        print("Body Test Profile")