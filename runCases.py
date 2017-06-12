import unittest
from cases import getTVChannal

class Run(unittest.TestCase):
    def suite(self):
        suit = unittest.TestSuite()
        suit.addTest(getTVChannal.GetTVChannal("test_getTVChannal"))
        return suit

if __name__ == "__main__":
    unittest.main(defaultTest="suit")
