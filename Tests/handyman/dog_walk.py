import unittest
import time
from .handyman_functions import *


class TestDogWalk(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver('sign-in')

    def test_chores_flow(self):
        try: 
            enter_info(self.driver)
            time.sleep(2)
            click_service_by_text(self.driver,'Dog Walking')
            time.sleep(5)
            next_button_for_cleaning1(self.driver)
            time.sleep(2)
            date_selection_box(self.driver)
            time.sleep(2)
            date_selection(self.driver,28)
            time.sleep(2)
            info_dogwalk(self.driver,'test name','7','random')
            checkout(self.driver)
            final_buttons(self.driver,'Confirm')

            time.sleep(10)

        except Exception as e:
            print(f"An error occurred: {e}")
        def tearDown(self):
            self.driver.quit()
        

if __name__ == "__main__":
        unittest.main()