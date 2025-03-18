from utils.Functions import (
    initialize_driver,
    enter_info,  
)
from .settings_functions import *

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver)
        time.sleep(5)
        settings(driver)
        time.sleep(4)
        setting_one(driver)
        time.sleep(1)
        setting_two(driver)
        time.sleep(3)
        third_setting(driver)
        time.sleep(2)
        fourth_setting(driver)
        time.sleep(2)
        #fifth_setting(driver)
        sixth_setting(driver)
        seventh_setting(driver)
        eigth_setting(driver)
        nineth_setting(driver)
        #settings_common(driver)
        
    

        time.sleep(10)
    

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

