#This is chores cleaning edit flow, testing here before addin to main file called chores.py
import time
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
    next_button_for_cleaning1,
    date_selection,
    final_button_chore, #remove if not used
    last_next_button,
    add_ons,
    checkout,
    pro_tip,
    submit,
    check
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
        choose_type(driver,'single')  
        time.sleep(2)
        cleaning_popup_button(driver) # ADD THIS TO THE ABOVE FUNCTION LATER
        time.sleep(2)
        next_button_for_cleaning1(driver)
        time.sleep(2)
        date_selection(driver, 29)
        time.sleep(2)
        next_button_for_cleaning1(driver)
        time.sleep(2)
        add_ons(driver) #CHECK THIS , GIVING PROBLEM
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
