#This is standard cleaning flow ...UPDATED ON 13TH JAN 
import time
from Functions import (
    click_element_by_xpath,
    add_ons,
    final_next_cleaning,
    promocode,
    final_button_cleaning
)

from chores_functions import (
    initialize_driver,
    enter_info,
    #click_cleaning_service,
    change_bedroom_bathroom,
    change_unit_number,
    click_next_button,
    click_skip_button,
    service_selection,
    second_next_button,
    click_service_by_text,
    choose_type,
    next_button_for_cleaning1,
    date_selection,
    final_button_chore,
    cleaning_popup_button
    
)

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver, 'aduggal+gcp2@amenify.com', 'Akulduggal46@123456')
        time.sleep(1)
        click_service_by_text(driver,'Cleaning')
        time.sleep(2)
        change_unit_number(driver, '3')
        change_bedroom_bathroom(driver, 1, 1)
        click_next_button(driver)
        click_skip_button(driver)
        service_selection(driver,"Standard")
        second_next_button(driver)
        choose_type(driver,'single')
        time.sleep(2)
        cleaning_popup_button(driver)
        next_button_for_cleaning1(driver)
        date_selection(driver, 31)
        time.sleep(3)
        final_button_chore(driver) #change name to a commonn name.
        add_ons(driver) #MAKES IT COMPULSARY, MAKE IT THAT ITS A CHOICE
        final_next_cleaning(driver)
        #FINAL CHECKOUT SCREEN
        #promocode(driver,'OFF') the service fee box is glitching here.
        final_button_cleaning(driver)


        # To be able to click the add instruction button 

        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
