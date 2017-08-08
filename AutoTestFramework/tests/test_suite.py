import unittest
from AutoTestFramework.tests.home.test_login import LoginTests
from AutoTestFramework.tests.home.test_courses import CoursesTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CoursesTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)