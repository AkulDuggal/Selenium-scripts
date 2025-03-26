import time
from .handyman_functions import *


def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver)
        time.sleep(2)
        click_service_by_text(driver,'Handyman')
        time.sleep(5)
        next_button_for_cleaning1(driver)
        time.sleep(2)
        date_selection_box(driver)
        time.sleep(2)
        date_selection(driver,28)
        time.sleep(2)
        checkout(driver)
        final_buttons(driver,'Confirm')

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        #driver.quit()
        time.sleep(30)

if __name__ == "__main__":
    main()