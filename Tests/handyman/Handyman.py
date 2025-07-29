import unittest
import time
from .handyman_functions import *


class TestHandyman(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver('sign-in')

    def test_chores_flow(self):
        try:
            enter_info(self.driver)
            time.sleep(2)
            click_service_by_text(self.driver,'Handyman')
            time.sleep(5)
            next_button_for_cleaning1(self.driver)
            time.sleep(2)
            date_selection_box(self.driver)
            time.sleep(2)
            date_selection(self.driver,28)
            time.sleep(2)
            checkout(self.driver)
            final_buttons(self.driver,'Confirm')

        except Exception as e:
            print(f"An error occurred: {e}")
        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()