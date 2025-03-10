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
    #look into this,, why is it not working
    
    print("******************123")
    time.sleep(10)
    print("******************456")
    script="""
    console.log("CHAL RAHHI HAI");
const divs = document.querySelectorAll('button');
divs.forEach(div => {
  if (div.textContent.trim() === 'OK') {
  console.log("MILGYA");
    div.click(); 
  }
  console.log("BAKWAAS");
});
"""
    
    driver.execute_script(script)
    print("OK button clicked successfully!")



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

        next_button_for_cleaning1(driver)

        time.sleep(1000)



    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        #driver.quit()
        time.sleep(300000)

if __name__ == "__main__":
    main()