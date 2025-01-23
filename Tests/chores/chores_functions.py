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

#FIRST NEXT BUTTON
def click_next_button(driver):
    next_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Next')]"))
    )
    next_button.click()
    print("Moved to next page, from first click function")


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
def chores_popup_button(driver):
    try:
        okay_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='button']")))
        okay_button.click()
        print("this is from popup function")

    except ElementClickInterceptedException:
        print("Element click intercepted by popup. Attempting to close popup...")
    
# This clicks the next button 
def next_button_for_chores(driver):
    script = """
const divs = document.querySelectorAll('div');
divs.forEach(div => {
  if (div.textContent.trim() === 'Next') {
    div.click();
  }
});
"""
    driver.execute_script(script)
    print("function ended, button clicked")

#this selects the date according to mentioned date
def date_selection(driver,index):
   
    xpath = f"(//div[@class='css-175oi2r r-1awozwy r-13awgt0'])[{index}]"
    
    
    div_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    
    
    div_element.click()
    print(f"Clicked the div element at index {index}")

#this will click checkout, change name for cleaning and chores
def final_button_chore(driver):
    '''done = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'Next')]")) #18th DECEMBER..CHANGED FRO CLEANING , CHECK CHORES
    )
    done.click()
    print("Chore flow complete")'''
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-175oi2r') and .//span[text()='Next']]"))
        )
        next_button.click()
        print("clicked")
    except Exception as e:
        
        print(f"Error: Could not click the 'Next' button - {str(e)}")
        raise Exception("Failed to click the 'Next' button. Check if it's present and clickable.")
    

def add_ons(driver):
        standard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1uavh4e r-42olwf r-z2wwpe r-rs99b7 r-5oul0u r-w7s2jr r-1qhn6m8 r-eoizbr'])[8]"))
            )     
        standard.click() 
        print("first addon selected")  
        
        standard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1uavh4e r-42olwf r-z2wwpe r-rs99b7 r-5oul0u r-w7s2jr r-1qhn6m8 r-eoizbr'])[9]"))
            ) 
        standard.click()
        print("second addon added")

        standard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1uavh4e r-42olwf r-z2wwpe r-rs99b7 r-5oul0u r-w7s2jr r-1qhn6m8 r-eoizbr'])[10]"))
            ) 
        standard.click()
        print("third addon added")

def last_next_button(driver):
    script = """
const nextButton = document.querySelector('div.css-175oi2r.r-1i6wzkk.r-lrvibr.r-1loqt21.r-1otgn73.r-1awozwy.r-udypu6.r-cayec9.r-18c69zk.r-1yadl64.r-18u37iz.r-1cmwbt1.r-1777fci.r-ytbthy.r-284m6k.r-iyfy8q span.css-1jxf684.r-fdjqy7');
if (nextButton) {
  nextButton.click();
} else {
  console.log("Next button not found!");
}
"""

# Execute the JavaScript
    driver.execute_script(script)

def checkout(driver):
    button=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[contains(text(),'Confirm')])[1]"))
    )
    button.click()
    print("checkout complete")
    time.sleep(10)


def pro_tip(driver, tip):
    
    button=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//span[normalize-space()='Service Pro Tip:'])[1]"))
    )
    button.click()
    print("pro tip clicked")
    time.sleep(5)
    if tip>0:
        button=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,f"(//div[@class='css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-a1yn9n r-1mwlp6a r-1777fci r-8dgmk1 r-18tzken'])[{tip}]"))
        )
        button.click()
        print("Tips added clicked")
        time.sleep(5)

        tips_submit=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[contains(text(),'Save Tip')])[1]"))
        )
        tips_submit.click()
        print("clicked button")
        time.sleep(5)

    else:
        button=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[contains(text(),'Close')])[1]"))
        )
        button.click()
        print("closed pro tip page")
        time.sleep(10)

def submit(driver):
    '''input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder=' '][value='yes']"))  #check how to correct this, this wont allow change in instructions
        )

    input_field.clear()
    input_field.send_keys("from selenium")

    print("Input value changed successfully!")'''
    time.sleep(5)
    submit_button=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[contains(text(),'Submit to continue')])[1]"))
    )
    submit_button.click()
    print("button clicked")
    time.sleep(5)

def check(driver):
    button=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//button[@role='button'])[3]"))
    )
    button.click()
    print("viewing the appointment page")
    time.sleep(2)


def checklist(driver):
    items=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1uavh4e r-42olwf r-z2wwpe r-rs99b7 r-5oul0u r-w7s2jr r-1qhn6m8 r-eoizbr'])[4]"))
        )
    items.click()
    print("added to checklist")

    '''item=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1uavh4e r-42olwf r-z2wwpe r-rs99b7 r-5oul0u r-w7s2jr r-1qhn6m8 r-eoizbr'])[5]"))
        )
    item.click()
    print("added to checklist")

    item=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1uavh4e r-42olwf r-z2wwpe r-rs99b7 r-5oul0u r-w7s2jr r-1qhn6m8 r-eoizbr'])[6]"))
        )
    item.click()
    print("added to checklist")'''
    time.sleep(2)

    