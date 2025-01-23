import time
from Utils.chores_functions import(
    initialize_driver,
    enter_info,
    click_service_by_text,
    change_bedroom_bathroom,
    change_unit_number,
    click_next_button,
    second_next_button,
    choose_type,
    cleaning_popup_button,
    date_selection,
    final_button_chore
)
from Utils.Functions import (
    second_next_button_chores,
    selecting_chores,
    date_selection,
    checkout_button,
    promocode,
    final_button_chore,
    #chores_popup_button,
    
)

def main():
    driver=initialize_driver('sign-in')
    try:
        enter_info(driver)
        click_service_by_text(driver,'Chores')
        change_unit_number(driver, '1')
        change_bedroom_bathroom(driver, 2, 3)
        click_next_button(driver)
        choose_type(driver,'single')
        time.sleep(2)
        cleaning_popup_button(driver)
        #chores_popup_button(driver) #this is not working, hence flow is incomplete
        second_next_button_chores(driver)
        selecting_chores(driver)
        second_next_button(driver)
        date_selection(driver, 30) #change according to the date to be selected 
        checkout_button(driver)
        promocode(driver,'OFF')
        final_button_chore(driver)
        

        # To be able to click the add instruction button 
        
        
        


        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()



