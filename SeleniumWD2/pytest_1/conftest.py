import pytest


@pytest.fixture()
def setUp():
    print("method running before each test")
    yield
    print("method running after each test")


@pytest.fixture(scope="module")
def oneTimeSetUp(browser, osType, request):
    print("method running before each test class")
    yield
    print("method running after each test class")

