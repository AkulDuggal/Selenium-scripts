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
import json

with open("config.json", "r") as file:
    config = json.load(file)

EMAIL = config["email"]
PASSWORD = config["password"]

def initialize_driver(access_type):
    driver = webdriver.Chrome()
    if access_type=='sign-up':
        driver.get('https://m.joinamenify.com/sign-up')
    elif access_type=='sign-in':
        driver.get('https://m.joinamenify.com/sign-in')
    else:
        driver.quit()
    return driver
# TO SELF, CHANGE FOR SIGNUP .. 
def enter_info(driver):
    if "sign-up" in driver.current_url:
        time.sleep(10)
        script = """
const buttons = document.querySelectorAll('div');
buttons.forEach(button => {
  if (button.textContent.trim() === 'Continue') {
    button.click();
    console.log('Continue button clicked.');
  }
});
"""
        driver.execute_script(script)
        print("Function ended, button clicked")
    else: 
        print("No box to click")

    input_fields = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[data-testid='text-input-flat']"))
    )
    input_field_email = input_fields[0]
    input_field_email.clear()
    input_field_email.send_keys(EMAIL)

    input_field_password = input_fields[1]
    input_field_password.clear()
    input_field_password.send_keys(PASSWORD)

    # Make decisions based on the current URL
    current_url = driver.current_url
    if 'sign-in' in current_url:
        print("Navigated to the Sign-In page.")
        sign_in_next = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Sign in')])[1]"))
        )
        sign_in_next.click()

    elif 'sign-up' in current_url:
        print("Navigated to the Sign-Up page.")
        tick_box=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='css-146c3p1 r-lrvibr']"))
        )
        tick_box.click()

        submit_button=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[contains(text(),'Continue')])[2]"))
    )
        submit_button.click()
        print("button clicked")
    else:
        print("Unexpected URL!")
        driver.quit()
        return None
    
    return driver


def click_service_by_text(driver, service_text):
    try:
        service = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[normalize-space()='{service_text}']"))
        )
        service.click()
        print(f"'{service_text}' service clicked successfully")
    except Exception as e:
        print(f"Failed to click the '{service_text}' service")

def cleaning_popup_button(driver):
    try:
        okay_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@swal-button='fdprocessedid']")))
        okay_button.click()
        print("this is from popup function")

    except ElementClickInterceptedException:
        print("Element click intercepted by popup. Attempting to close popup...")


def next_button_for_cleaning1(driver):
    
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