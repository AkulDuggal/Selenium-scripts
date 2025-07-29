import unittest
from .Handyman import TestHandyman
from .dog_walk import TestDogWalk

def run_test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(TestDogWalk),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestHandyman),
    ])

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_test_suite()
