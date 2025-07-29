import unittest
from .chores import TestChores
from .subscription_chores import TestChoresSub

def run_test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(TestChores),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestChoresSub),
    ])

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_test_suite()
