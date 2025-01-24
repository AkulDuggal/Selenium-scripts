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
        second_next_button_chores(driver)
        selecting_chores(driver) #hard coded names, fix later
        second_next_button_chores(driver)
        date_selection(driver, 30)
        checkout_button(driver)
        pro_tip(driver,1) #hard coded the value in xpath
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



