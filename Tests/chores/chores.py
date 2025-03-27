import unittest
import time
from .chores_functions import *
    
class TestChores(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver('sign-in')
    
    def test_chores_flow(self):
        try:
            enter_info(self.driver)
            time.sleep(2)
            click_service_by_text(self.driver,'Chores')
            change_unit_number(self.driver, '1')
            change_bedroom_bathroom(self.driver, 2, 3)
            click_next_button(self.driver)
            choose_type(self.driver,'single')
            time.sleep(2)
            chores_popup_button(self.driver)
            time.sleep(2)
            second_next_button_chores(self.driver)
            time.sleep(2)
            #new_chores_list(self.driver)
            selecting_chores(self.driver)
            time.sleep(4)
            second_next_button_chores(self.driver)
            time.sleep(4)
            date_selection(self.driver, 30)
            time.sleep(2)
            checkout_button(self.driver)
            time.sleep(2)
            pro_tip(self.driver,1) #hard coded the value in xpath
            time.sleep(2)
            checkout(self.driver)
            time.sleep(2)
            submit(self.driver)
            check(self.driver)
        
        #promocode(driver,'OFF')
            time.sleep(10)

        except Exception as e:
            print(f"An error occurred: {e}")
        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()



