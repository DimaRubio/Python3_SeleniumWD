import unittest
from SeleniumWD2.unit_test_sec25.test_сlass2 import TestClass2
from SeleniumWD2.unit_test_sec25.test_class1 import TestClass1

loader = unittest.TestLoader()
#get all test cases contained in TestClass1, TestClass2 in separate test suite
ts1 = loader.loadTestsFromTestCase(TestClass1)
ts2 = loader.loadTestsFromTestCase(TestClass2)
#aggregate several test suite
smoke_test_suite = unittest.TestSuite([ts1, ts2])

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(smoke_test_suite)
