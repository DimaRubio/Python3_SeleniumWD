"""For run this test case type to command line "py.test -v -s pytest_1/test_case_2.py"
   or "py.test -v -s pytest_1/test_case*.py" in project directory
"""
import pytest


@pytest.mark.run(order=1)
def test_C(oneTimeSetUp, setUp):
    print("Body test C")


@pytest.mark.run(order=3)
def test_E(oneTimeSetUp, setUp):
    print("Body test E")


@pytest.mark.run(order=4)
def test_F(oneTimeSetUp, setUp):
    print("Body test F")


@pytest.mark.run(order=2)
def test_D(oneTimeSetUp, setUp):
    print("Body test D")