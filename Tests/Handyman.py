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
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

from utils.Functions import (
    initialize_driver,
    enter_info,
    click_service_by_text,
    corner_click
  
)

def cleaning_popup_button(driver):
    try:
        okay_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@swal-button='fdprocessedid']")))
        okay_button.click()
        print("this is from popup function")

    except ElementClickInterceptedException:
        print("Element click intercepted by popup. Attempting to close popup...")


def next_button_for_cleaning1(driver):
    script = """
setTimeout(() => {
  document.querySelectorAll('.swal-button.swal-button--confirm').forEach(button => {
    if (button.innerText.trim() === 'OK') {
      button.click();
      console.log('Button clicked');
    }
  });
}, 500); // Delay to ensure the button is present
"""
    driver.execute_script(script)
    print("Function ended, button clicked")



def trying(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "swal-modal"))
    )

    # Wait for the OK button and click it
    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'swal-button') and contains(@class, 'swal-button--confirm') and text()='OK']"))
    )
    ok_button.click()
    print("OK button clicked successfully.")

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
        enter_info(driver)
        time.sleep(2)

        #HANDYMAN TESTING
        #first_window=driver.current_window_handle
        time.sleep(2)
        click_service_by_text(driver,'Handyman')
        time.sleep(5)

        trying(driver)
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