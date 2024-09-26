import time
from Functions import (
    initialize_driver,
    enter_info,
    click_service_by_text,
    change_bedroom_bathroom,
    change_unit_number,
    click_next_button,
    choose_type,
    second_next_button_chores,
    selecting_chores,
    second_next_button,
    date_selection
)

def main():
    driver=initialize_driver('sign-in')
    try:
        enter_info(driver,'aduggal@amenify.com', 'Akulduggal46@123456')
        click_service_by_text(driver,'Chores')
        change_unit_number(driver, '1')
        change_bedroom_bathroom(driver, 2, 3)
        click_next_button(driver)
        choose_type(driver,'single')
        second_next_button_chores(driver)
        selecting_chores(driver)
        second_next_button(driver)
        date_selection(driver, 30) #change according to the date to be selected 
        #selecting date after chores selection
        


        


        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()



