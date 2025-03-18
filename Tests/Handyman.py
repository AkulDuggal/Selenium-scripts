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
    # Get current window handles
    current_window = driver.current_window_handle
    all_windows = driver.window_handles

# Switch to the new window (assuming it's the last one opened)
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            break

# Now execute the script after switching
    script = """
    console.log("WORKING");
    const divs = document.querySelectorAll('button');
    divs.forEach(div => {
        if (div.textContent.trim() === 'OK') {
            console.log("FOUND");
            div.click();
        }
        console.log("DIDNT WORK");
    });
"""

# Run the script in the new window
    driver.execute_script(script)
    print("OK button clicked successfully!")

def date_selection_box(driver):
    date_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//input[@id='dpDate'])[1]")))
    date_button.click()
    print("date box clicked") 

def date_selection(driver,date):
    div_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"(//a[normalize-space()='{date}'])[1]"))
        )
    
    div_element.click()
    print(f"Clicked the div element at index {date}")

def checkout(driver):
    button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='create-order-btn'])[1]")))
    button.click()
    print("button clicked")


def final_buttons(driver,text):
    button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, f"(//button[normalize-space()='{text}'])[1]")))
    button.click()


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
        time.sleep(2)
        date_selection_box(driver)
        time.sleep(2)
        date_selection(driver,28)
        time.sleep(2)
        checkout(driver)
        final_buttons(driver,'Confirm')

        time.sleep(10)



    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        #driver.quit()
        time.sleep(30)

if __name__ == "__main__":
    main()