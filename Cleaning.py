#This is standard cleaning flow
import time
from Functions import (
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
    click_element_by_xpath,
    choose_type,
    next_button_for_cleaning1,
    date_selection,
    final_button_chore,
    selecting_chores
    
    
)

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver, 'aduggal@amenify.com', 'Akulduggal46@123456')
        time.sleep(1)
        click_service_by_text(driver,'Cleaning')
        time.sleep(2)
        change_unit_number(driver, '3')
        change_bedroom_bathroom(driver, 1, 1)
        click_next_button(driver)
        click_skip_button(driver)
        service_selection(driver)
        second_next_button(driver)
        choose_type(driver,'single')
        next_button_for_cleaning1(driver)
        date_selection(driver, 30)
        time.sleep(3)
        final_button_chore(driver) #change name to a commonn name.
        #need to add for selecting chore.
    
        #didnt work
        selecting_chores(driver) # find a common name, also add ways to select which chore to select




        

        

        
       



        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
