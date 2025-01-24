from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from Utils.Functions import (
    initialize_driver,
    enter_info,
    amenify_one,
    amenify_credits
    
)
#HAS AMENIFY ONE SUBSCRIPTION, GIFT CARD AND DISCOUNTED CREDITS.
def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver, 'aduggal@amenify.com', 'Akulduggal46@123456')
        time.sleep(2)

        '''amenify_one(driver)
        #can add assertion here for succesfully bought sub message.
        print("Amenify sub bought")
        time.sleep(10)''' # need to find a way to put this in if/else as it only happens onc a month.

        amenify_credits(driver,'50',"Credits") # Choose between Credits/Card
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

