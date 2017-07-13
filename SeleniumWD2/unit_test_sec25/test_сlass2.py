import unittest

class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*"*10,"Before Class 2","*"*10)

    @classmethod
    def tearDownClass(cls):
        print("*"*10,"After Class 2","*"*10)

    def setUp(self):
        print("Before every test in Class 2")

    def tearDown(self):
        print("After every test in Class 2")

    def test_C(self):
        print("TestC")
        list_obj={"aaa","bbb","ccc", 10}
        self.assertIn(10,list_obj,"not consisted in list")

    def test_D(self):
        print("TestD")
        s1 = "hello amazing python word"
        self.assertIn("python", s1,"not consisted in list")

if __name__ == '__main__':
    unittest.main(verbosity=2)



