from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

from Functions import (
    initialize_driver,
    enter_info,
    click_service_by_text,
    corner_click
  
)



def perform_mouse_actions(driver, *coordinates):
    """
    Moves the mouse to each (x, y) coordinate in `coordinates` and clicks.

    Args:
        driver: Selenium WebDriver instance.
        *coordinates: Variable length argument list of (x, y) tuples for click locations.
    """
    actions = ActionChains(driver)

    for (x, y) in coordinates:
        # Move the mouse to the specified coordinates
        pyautogui.moveTo(x, y)
        time.sleep(0.5)  # Pause to allow movement, adjust as needed

        # Perform a click at the current location
        actions.click().perform()
        time.sleep(0.5)

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver, 'aduggal+nov1@amenify.com', 'Akulduggal46@123456')
        time.sleep(2)

        #HANDYMAN TESTING
        #first_window=driver.current_window_handle
        time.sleep(2)
        click_service_by_text(driver,'Handyman')
        time.sleep(5)

        perform_mouse_actions(driver, (10, 10), (220, 220))

        print("pop up closed")

        '''done=WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.XPATH,"(//button)"))
        )
        done[2].click()
        time.sleep(5)
        print("pop up closed ")'''

       




        time.sleep(10)



    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()