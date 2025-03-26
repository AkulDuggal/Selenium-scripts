#This is standard cleaning subscription flow ..
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
        service_selection(driver,"Standard")
        time.sleep(2)
        second_next_button(driver)
        time.sleep(2)
        choose_type(driver,'multi')  
        time.sleep(2)
        next_button_for_cleaning1(driver) #causin loop, check
        time.sleep(2)
        #new_chores_list(driver) # fix this later
        add_ons(driver)
        time.sleep(2)
        next_button_for_cleaning1(driver)
        time.sleep(2)
        checkout(driver)
        time.sleep(4)
        submit(driver)
        time.sleep(4)
        check(driver)
        print("flow complete")

        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
