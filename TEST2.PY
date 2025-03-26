# Use this file to create food/grocery  functions and test them 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time
from selenium.webdriver.common.action_chains import ActionChains
import json

with open("config.json", "r") as file:
    config = json.load(file)

EMAIL = config["email"]
PASSWORD = config["password"]

#THIS IS FOR OPENING THE WINDOW WITH AMENIFY STAGE
def initialize_driver(access_type):
    driver = webdriver.Chrome()
    if access_type=='sign-up':
        driver.get('https://m.joinamenify.com/sign-up')
    elif access_type=='sign-in':
        driver.get('https://m.joinamenify.com/sign-in')
    else:
        driver.quit()
    return driver


#THIS IS FOR LOGIN AND SIGNUP
def enter_info(driver):
    if "sign-up" in driver.current_url:
        Messagebox=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[2]"))
    ).click()
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

    #CHECK THIS , NEEDS TO BE UPDATED
    elif 'sign-up' in current_url:
        print("Navigated to the Sign-Up page.")
        tick_box=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='css-146c3p1 r-lrvibr']"))
        )
        tick_box.click()

        sign_in_next = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='css-175oi2r r-1phboty']"))
        )
        sign_in_next.click()
    else:
        print("Unexpected URL!")
        driver.quit()
        return None
    
    return driver

#THIS FUNCTION CLICKS THE SERVICE MENTIONED
def click_service_by_text(driver, service_text):
    try:
        service = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[normalize-space()='{service_text}']"))
        )
        service.click()
        print(f"'{service_text}' service clicked successfully")
    except Exception as e:
        print(f"Failed to click the '{service_text}' service")


def type(driver,text):
    current_window = driver.current_window_handle
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            break
    type=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, f"(//span[normalize-space()='{text}'])[1]")))
    type.click()
    print(f"{text} clicked")
    
    
def final_store(driver):
    time.sleep(5)
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    if len(iframes) > 0:
        driver.switch_to.frame(iframes[0])  # Switch to the correct iframe
        print("Switched to iframe 0.")
    else:
        print("No iframes found!")
        return

    # Updated JavaScript to run within the iframe
    script = """
const stores = document.querySelectorAll(".store-overview-item-3");
if (stores.length > 0) {
    stores[0].click();  // Click the first store directly
    console.log("First store clicked successfully!");
} else {
    console.log("No store entries found.");
}
"""
    # Execute the script inside the iframe
    driver.execute_script(script)
    print("Store clicked successfully!")

    # Switch back to the main content after executing JS
    driver.switch_to.default_content()

def store_test(driver):
    time.sleep(5)
    
    # Switch directly to iframe 0
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    if len(iframes) > 0:
        driver.switch_to.frame(iframes[0])
        print("Switched directly to iframe 0.")
    else:
        print("No iframes found!")
        return
    
    # Wait for store elements to load in iframe 0
    try:
        stores = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "store-overview-item-3"))
        )
        print(f"Number of stores found: {len(stores)}")
        
        if len(stores) > 0:
            # Click the first store (index 0, not 1)
            stores[1].click()
            print("First store clicked successfully!")
        else:
            print("No store entries found.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Switch back to main content
    driver.switch_to.default_content()



def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver)
        time.sleep(6)
        click_service_by_text(driver,'Food / Grocery')
        time.sleep(10)
        type(driver,'Food')
        time.sleep(2)
        #these both work, keeping here as sometimes they dont work
        #store_test(driver)
        #final_store(driver)
        time.sleep(5)





        time.sleep(10)
    
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()