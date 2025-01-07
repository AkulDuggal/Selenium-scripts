#This is standard cleaning edit flow,  THIS BEFORE ADDING IN MAIN FILE NAMED: Cleaning.py
import time
from Functions import (
    #initialize_driver,
    #enter_info,
    #click_cleaning_service,
    #change_bedroom_bathroom,
    #change_unit_number,
    #click_next_button,
    #click_skip_button,
    #service_selection,
    #second_next_button,
    #click_service_by_text,
    click_element_by_xpath,
    #choose_type,
    #next_button_for_cleaning1,
    date_selection,
    final_button_chore,
    add_ons,
    final_next_cleaning,
    promocode,
    final_button_cleaning   
)
from chores_functions import(
    initialize_driver,
    enter_info,
    click_service_by_text,
    change_bedroom_bathroom,
    change_unit_number,
    click_next_button,
    click_skip_button,
    service_selection,
    second_next_button,
    choose_type,
    cleaning_popup_button,
    next_button_for_cleaning1
)

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver, 'aduggal+gcp2@amenify.com', 'Akulduggal46@123456')
        time.sleep(6)
        click_service_by_text(driver,'Cleaning')
        time.sleep(1)
        change_bedroom_bathroom(driver, 4, 2)
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
        choose_type(driver,'multi')  #the pop up is not interactable at all...so using sub
        time.sleep(2)
        #cleaning_popup_button(driver) this is not working what so ever
        next_button_for_cleaning1(driver)
        



        '''
        
        time.sleep(2)
        
        
        
        
        
        
        next_button_for_cleaning1(driver)
        date_selection(driver, 31)
        time.sleep(3)
        final_button_chore(driver) #change name to a commonn name.
        add_ons(driver) #MAKES IT COMPULSARY, MAKE IT THAT ITS A CHOICE
        final_next_cleaning(driver)
        #FINAL CHECKOUT SCREEN
        #promocode(driver,'OFF') the service fee box is glitching here.
        final_button_cleaning(driver)'''


        # To be able to click the add instruction button 

        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
