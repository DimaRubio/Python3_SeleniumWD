import pytest


@pytest.fixture()
def setUp():
    print("Method running before each test")
    yield
    print("Method running after each test")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print("Method running before each class")
    if browser == 'firefox':
        print("Running tests on FF")
        value = 10
    elif browser == 'safary':
        print("Running tests on safary")
        value = 20
    else:
        print("Running tests on chrome")
        value = 30
    if request.cls is not None:
        request.cls.value = value
    yield value
    print("Method running after each class")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
