import unittest

class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("asfasfasf")
        print("*"*10,"Before Class 1","*"*10)

    @classmethod
    def tearDownClass(cls):
        print("*"*10,"After Class 1","*"*10)

    def setUp(self):
        print("Before every test in Class 1")

    def tearDown(self):
        print("After every test in Class 1")

    def test_A(self):
        print("TestA")
        a = True
        b = False
        self.assertFalse(a and b, "something go wrong")

    @unittest.skip("test skipping for example")
    def test_B(self):
        print("TestB")
        a = 10
        b = 101
        self.assertNotEqual(a,b)

if __name__ == '__main__':
    unittest.main(verbosity=2)

    # 0 (quiet): you just get the total numbers of tests executed and the global result
    # 1 (default): you get the same plus a dot for every successful test or a F for every failure
    # 2 (verbose): you get the help string of every test and the result



