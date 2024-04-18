import unittest


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这是测试整个类前要执行的方法")

    def setUp(self):
        print("这是每一个测试方法前面运行的方法")

    def tearDown(self):
        print("这是每一个测试方法后面运行的方法")

    def test_class1(self):
        print("这是方法1")

    def test_class2(self):
        print("这是方法2")

    @classmethod
    def tearDownClass(cls):
        print("这是测试整个类后要执行的方法")

if __name__ =='__main__':
    test = TestClass()

