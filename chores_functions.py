# PURPOSE OF THIS FILE IS TO FIX CHORES FUNCTION AND STANDARDIZE THE FUNCTIONS LIMITED TO CHORES ONLY
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
def enter_info(driver, email, password):
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
    input_field_email.send_keys(email)

    input_field_password = input_fields[1]
    input_field_password.clear()
    input_field_password.send_keys(password)

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

# THIS FUNCTION CHANGES THE BED AND BATH AS MENTIONED
def change_bedroom_bathroom(driver, num_bedrooms, num_bathrooms):
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//select[@data-testid='web_picker']"))
    )
    select_bedroom = Select(dropdown[0])
    select_bedroom.select_by_visible_text(f'{num_bedrooms} bed(s)')

    select_bathroom = Select(dropdown[1])
    select_bathroom.select_by_visible_text(f'{num_bathrooms} bath(s)')

#THIS FUNCTION CHANGES UNIT NUMBER
def change_unit_number(driver, unit_number):
    unit_number_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='text-input-flat']"))
    )
    unit_number_field.click()
    unit_number_field.send_keys(Keys.CONTROL + "a")  
    unit_number_field.send_keys(unit_number)

#fIRST NEXT BUTTON
def click_next_button(driver):
    next_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Next')]"))
    )
    next_button.click()
    print("Moved to next page, from first click function")

#THIS IS THE SKIP BUTTON TO MOVE AHEAD
def click_skip_button(driver):
    next_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Skip')]"))
    )
    next_button.click()
    print("Moved to next page, from skip click function")

#THIS SELECTS SERVICE TYPE
def service_selection(driver,service_text):
    standard = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//div[normalize-space()='{service_text}']"))
    )
    standard.click()
    print(f"Clicked '{service_text}' service")

#CLICKS THE SECOND NEXT BUTTON
def second_next_button(driver): 
    time.sleep(1)   
    standard = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Next'])[1]"))
    )
    #(//span[normalize-space()='Next'])[1]
    time.sleep(1)
    standard.click()
    print("Clicked next button from the second function")

#THIS FUNCTION CHOOSES ONE TIME OR SUB
def choose_type(driver,type):
    current_url=driver.current_url

    if type=="single":
        element=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'One-time appointment')]"))
        )
        element.click()

        '''element=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"(//div[@class='css-175oi2r r-1awozwy r-18u37iz r-1777fci'])[12]"))
        )
        element.click()'''


    elif type=="multi":
        #need if/else as chores only has 3 sub options for stage.
        if 'cleaning' in current_url:
            element=WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,"(//div[contains(@class, 'css-146c3p1 r-fdjqy7') and contains(normalize-space(), 'Subscription')])[4]"))
                )
            element.click()
        else:
            element=WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,"(//div[contains(@class, 'css-146c3p1 r-fdjqy7') and contains(normalize-space(), 'Subscription')])[3]"))
                )
            element.click()

    else:
        print("no service available")
        driver.quit()

#THIS SHOULD CLICK OK FOR CLEANING POPUP
def cleaning_popup_button(driver):
    time.sleep(2)
    try:
        okay_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='button']")))
        okay_button.click()

    except ElementClickInterceptedException:
        print("Element click intercepted by popup. Attempting to close popup...")
    
def next_button_for_cleaning1(driver):

    try:
        time.sleep(2)  # Consider replacing this with an explicit wait

        # Wait for the "Next" button to be clickable
        standard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-1wtzoqk r-cayec9 r-1fuqb1j r-1yadl64 r-18u37iz r-1cmwbt1 r-1777fci r-6dt33c r-ywh0we r-284m6k r-iyfy8q'])"))
        )
        standard.click()
    
    except Exception as e:
        # Print the error message for debugging
        print(f"Error: Could not click the 'Next' button - {str(e)}")

        # Raise the exception so the script does not proceed silently
        raise Exception("Failed to click the 'Next' button. Check if it's present and clickable.")