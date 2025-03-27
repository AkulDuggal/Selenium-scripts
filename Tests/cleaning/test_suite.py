import unittest
#from .Cleaning import TestCleaning
#from .sub_cleaning import TestCleaningSub
from .flowtest import TestCleaning

def run_test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(TestCleaning),
        #unittest.defaultTestLoader.loadTestsFromTestCase(TestCleaningSub),
    ])

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_test_suite()
