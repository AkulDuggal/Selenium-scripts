#This is standard cleaning flow ...UPDATED ON 16TH JAN 
import time
from .cleaning_functions import *

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver)
        time.sleep(6)
        click_service_by_text(driver,'Cleaning')
        time.sleep(1)
        change_bedroom_bathroom(driver, 1, 1)
        change_unit_number(driver, '4')
        time.sleep(2)
        click_next_button(driver)
        time.sleep(2)
        click_skip_button(driver)
        time.sleep(2)
        service_selection(driver,"Standard")
        time.sleep(2)
        second_next_button(driver)
        time.sleep(2)
        choose_type(driver,'single')  
        time.sleep(2)
        cleaning_popup_button(driver) # ADD THIS TO THE ABOVE FUNCTION LATER
        time.sleep(2)
        next_button_for_cleaning1(driver)
        time.sleep(2)
        test_date_selection(driver, 29)
        time.sleep(2)
        next_button_for_cleaning1(driver)
        time.sleep(2)
        #add_ons(driver) #CHECK THIS , GIVING PROBLEM
        time.sleep(2)
        last_next_button(driver)
        time.sleep(2)
        pro_tip(driver,1)
        time.sleep(2)
        checkout(driver)
        time.sleep(2)
        submit(driver)
        time.sleep(2)
        check(driver)
        print("flow complete")


        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
