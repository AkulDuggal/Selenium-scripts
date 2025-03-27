import time
from .chores_functions import *
    
def main():
    driver=initialize_driver('sign-in')
    try:
        enter_info(driver)
        time.sleep(2)
        click_service_by_text(driver,'Chores')
        change_unit_number(driver, '1')
        change_bedroom_bathroom(driver, 2, 3)
        click_next_button(driver)
        choose_type(driver,'single')
        time.sleep(2)
        chores_popup_button(driver)
        time.sleep(2)
        second_next_button_chores(driver)
        time.sleep(2)
        selecting_chores(driver)
        #new_chores_list(driver)
        time.sleep(2)
        second_next_button_chores(driver)
        time.sleep(2)
        date_selection(driver, 30)
        time.sleep(2)
        checkout_button(driver)
        time.sleep(2)
        pro_tip(driver,1) #hard coded the value in xpath
        time.sleep(2)
        checkout(driver)
        time.sleep(2)
        submit(driver)
        check(driver)
        
        #promocode(driver,'OFF')
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()



