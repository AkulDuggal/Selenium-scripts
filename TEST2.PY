#This is chores cleaning edit flow, testing here before addin to main file called chores.py
import time
from chores_functions import(
    initialize_driver,
    enter_info,
    click_service_by_text,
    change_bedroom_bathroom,
    change_unit_number,
    click_next_button,
    choose_type,
    chores_popup_button,
    next_button_for_chores,
    date_selection,
    final_button_chore, #remove if not used
    last_next_button,
    add_ons,
    checkout,
    pro_tip,
    submit,
    checklist
)

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver, 'aduggal+gcp2@amenify.com', 'Akulduggal46@123456')
        time.sleep(6)
        click_service_by_text(driver,'Chores')
        time.sleep(1)
        change_bedroom_bathroom(driver, 1, 1)
        change_unit_number(driver, 'chores')
        time.sleep(2)
        click_next_button(driver)
        time.sleep(2)
        choose_type(driver,'single')  
        time.sleep(2)
        chores_popup_button(driver) # ADD THIS TO THE ABOVE FUNCTION LATER
        time.sleep(2)
        next_button_for_chores(driver)
        time.sleep(4)
        checklist(driver) # this is not working accuratly
        time.sleep(2)
        next_button_for_chores(driver)



        '''date_selection(driver, 29)
        time.sleep(2)
        next_button_for_cleaning1(driver)
        time.sleep(2)'''
        


        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
