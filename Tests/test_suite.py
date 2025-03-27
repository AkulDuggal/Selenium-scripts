import unittest
from chores.chores import TestChores
from chores.subscription_chores import TestChoresSub
from cleaning.Cleaning import TestCleaning
from cleaning.sub_cleaning import TestCleaningSub

def run_test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(TestChores),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestChoresSub),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestCleaning),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestCleaningSub),
    ])

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_test_suite()


    

