"""For run this test case type to command line "py.test -v -s pytest_1/test_case.py" in project directory
"""


def test_A(oneTimeSetUp, setUp): # Order of arguments is important
    print("test A")


def test_B(oneTimeSetUp, setUp):
    print("test B")