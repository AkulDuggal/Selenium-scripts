#test Flow to automate all 3 types together
#add seperate dates as same day different type appointments are not possible
import unittest
import time
from .cleaning_functions import *

class TestCleaning(unittest.TestCase):
    def run_cleaning_flow(self, service_type):
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
            
            # Service Selection (Dynamic Step)
            service_selection(self.driver, service_type)
            time.sleep(2)

            second_next_button(self.driver)
            time.sleep(2)
            choose_type(self.driver, 'single')
            time.sleep(2)
            cleaning_popup_button(self.driver)
            time.sleep(2)
            next_button_for_cleaning1(self.driver)
            time.sleep(2)
            date_selection(self.driver, 30)
            time.sleep(2)
            next_button_for_cleaning1(self.driver)
            time.sleep(2)
            add_ons(self.driver)
            time.sleep(2)
            last_next_button(self.driver)
            time.sleep(2)
            pro_tip(self.driver, 1)
            time.sleep(2)
            '''checkout(self.driver)
            time.sleep(2)
            submit(self.driver)
            time.sleep(2)
            check(self.driver)'''
            print(f"Flow complete for {service_type}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def setUp(self):
        self.driver = initialize_driver('sign-in')

    '''def test_standard_cleaning(self):
        self.run_cleaning_flow("Standard")'''

    def test_deep_cleaning(self):
        self.run_cleaning_flow("Deep")

    def test_move_out_cleaning(self):
        self.run_cleaning_flow("Move-Out") # not selecting date here

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
