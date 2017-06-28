import unittest
from cases.getTVChannal import GetTVChannal
from cases.checkQQOnline import CheckQQOnline


class Run(unittest.TestCase):
    def run(self, result=None):
        suite1 = unittest.TestLoader().loadTestsFromTestCase(GetTVChannal)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(CheckQQOnline)
        suite = unittest.TestSuite([suite1, suite2])
        return suite


if __name__ == "__main__":
    # 此用法可以同时测试多个类
    unittest.TextTestRunner(verbosity=2).run(Run())
