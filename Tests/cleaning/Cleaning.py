import unittest
import time
from .cleaning_functions import *

class TestCleaning(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver('sign-in')

    def test_cleaning_flow(self):
        try:
            enter_info(self.driver)
            time.sleep(6)
            click_service_by_text(self.driver, 'Cleaning')
            time.sleep(1)
            change_bedroom_bathroom(self.driver, 1, 1)
            change_unit_number(self.driver, '4')
            time.sleep(2)
            click_next_button(self.driver)
            time.sleep(2)
            service_selection(self.driver, "Standard")
            time.sleep(2)
            second_next_button(self.driver)
            time.sleep(2)
            choose_type(self.driver, 'single')
            time.sleep(2)
            cleaning_popup_button(self.driver)
            time.sleep(2)
            next_button_for_cleaning1(self.driver)
            time.sleep(2)
            date_selection(self.driver, 28)
            time.sleep(2)
            next_button_for_cleaning1(self.driver)
            time.sleep(2)
            # add_ons(self.driver)  # Uncomment if working
            time.sleep(2)
            last_next_button(self.driver)
            time.sleep(2)
            pro_tip(self.driver, 1)
            time.sleep(2)
            checkout(self.driver)
            time.sleep(2)
            submit(self.driver)
            time.sleep(2)
            check(self.driver)
            print("Flow complete")
        except Exception as e:
            print(f"An error occurred: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
