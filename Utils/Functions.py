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


def click_service_by_text(driver, service_text):
    try:
        service = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[normalize-space()='{service_text}']"))
        )
        service.click()
        print(f"'{service_text}' service clicked successfully")
    except Exception as e:
        print(f"Failed to click the '{service_text}' service")


def change_bedroom_bathroom(driver, num_bedrooms, num_bathrooms):
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//select[@data-testid='web_picker']"))
    )
    select_bedroom = Select(dropdown[0])
    select_bedroom.select_by_visible_text(f'{num_bedrooms} bed(s)')

    select_bathroom = Select(dropdown[1])
    select_bathroom.select_by_visible_text(f'{num_bathrooms} bath(s)')

def change_unit_number(driver, unit_number):
    unit_number_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='text-input-flat']"))
    )
    unit_number_field.click()
    unit_number_field.send_keys(Keys.CONTROL + "a")  
    unit_number_field.send_keys(unit_number)
    

def click_next_button(driver):
    next_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Next')]"))
    )
    next_button.click()
    print("Moved to next page, from first click function")

def click_skip_button(driver):
    next_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Skip')]"))
    )
    next_button.click()
    print("Moved to next page, from skip click function")


def service_selection(driver):
    standard = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[normalize-space()='Standard'])[1]"))
    )
    standard.click()
    print("Clicked standard service")

def second_next_button(driver): 
    time.sleep(1)   
    standard = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[9]"))
    )
    time.sleep(1)
    standard.click()
    print("Clicked next button from the second function")

def second_next_button_chores(driver): 
    time.sleep(1)   
    standard = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[8]"))
    )
    time.sleep(1)
    standard.click()
    print("Clicked next button from the second function")
    
def click_element_by_xpath(driver, xpath, delay_seconds):  # can use this to test if xpath is working...
    '''element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element.click()
    print(f"Clicked element with XPath: {xpath}")
    time.sleep(delay_seconds)'''
    time.sleep(1)   
    standard = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,xpath))
    )
    time.sleep(1)
    standard.click()
    print("Clicked next button from the second function")

def choose_type(driver,type):
    current_url=driver.current_url

    if type=="single":
        element=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'One-time appointment')]"))
        )
        element.click()

        element=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"(//div[@class='css-175oi2r r-1awozwy r-18u37iz r-1777fci'])[12]"))
        )
        element.click()


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

def test_function(driver): #test to successfully click the next button
    time.sleep(1)
    standard = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space(text())='Next']"))
    )
    time.sleep(3)
    standard.click()
    print("Clicked next button from the second function")


def selecting_chores(driver):
    standard = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "(//div[@class='css-175oi2r'])"))
    )

    #print(f"Number of elements found: {len(standard)}") 141 elements returned.
    
    standard[83].click()  # 84th element (index starts at 0)
    time.sleep(1)
    print("Clicked first chore")

    standard[89].click()  # 90th element
    time.sleep(1)
    print("Clicked second chore")

    standard[95].click()  # 96th element
    time.sleep(1)
    print("Clicked third chore")
    
    
def date_selection(driver,index):
    # Construct the dynamic XPath with the provided index
    xpath = f"(//div[@class='css-175oi2r r-1awozwy r-13awgt0'])[{index}]"
    
    # Wait for the element to be clickable
    div_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    
    # Click the located element
    div_element.click()
    print(f"Clicked the div element at index {index}")

def checkout_button(driver): 
    time.sleep(1)   
    standard = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[12]"))
    )
    time.sleep(1)
    standard.click()
    print("Clicked next button from the second function")

def next_button_for_cleaning1(driver):
    time.sleep(2)
    standard= WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[11]"))
    )
    time.sleep(1)
    standard.click()


def promocode(driver,code):
    next_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@autocapitalize='characters'])[1]"))
        )
    next_button.send_keys({code})
    print("ADDED PROMO CODE")
    time.sleep(5)
    apply_button=WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"(//div[@class='css-175oi2r r-1phboty r-15d164r'])[1]"))
        )
    apply_button.click()
    time.sleep(5)
    
    #service tip box selected
    tip=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-13awgt0 r-18u37iz'])[8]"))
        )   
    tip.click()

    #to close the tip box
    tip_close=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[15]"))
        )   
    tip_close.click()
    time.sleep(5)

    #to add tip(TO WORK ON)
    '''tip_amount=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"(//div[@class='css-175oi2r'])[219]"))
        )
    
    tip_amount.click()
    tip_amount.send_keys({amount})'''    
    

def final_button_chore(driver):
    done=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[13]")) #18th DECEMBER..CHANGED FRO CLEANING , CHECK CHORES
    )
    done.click()
    print("Chore flow complete")


def add_ons(driver):
        standard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1uavh4e r-42olwf r-z2wwpe r-rs99b7 r-5oul0u r-w7s2jr r-1qhn6m8 r-eoizbr'])[10]"))
            )     
        standard.click()   
        
        standard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1uavh4e r-42olwf r-z2wwpe r-rs99b7 r-5oul0u r-w7s2jr r-1qhn6m8 r-eoizbr'])[11]"))
            ) 
        standard.click()

        standard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1uavh4e r-42olwf r-z2wwpe r-rs99b7 r-5oul0u r-w7s2jr r-1qhn6m8 r-eoizbr'])[12]"))
            ) 
        standard.click()
#IF POSSIBLE, JOIN THESE 2 FUNCTIONS

def final_next_cleaning(driver):
    standard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[15]"))
        )
    standard.click() 
    time.sleep(1)
    print("Clicked next button")


def final_button_cleaning(driver):
    done=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[17]"))
    )
    done.click()
    time.sleep(5)
    print("Cleaning flow complete")


def amenify_one(driver):
    done=WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"(//div[@class='css-175oi2r r-1phboty r-1dzdj1l r-19jyx45 r-13qz1uu'])[1]"))
        )
    done.click()
        
    done1=WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"(//div[@class='css-175oi2r r-1awozwy r-18u37iz r-1777fci'])[6]"))
        )
    done1.click()
    time.sleep(5)
        #can add assertion here for succesfully bought sub message.
    print("Amenify sub bought")


    
def amenify_credits(driver, amount,type):
    if type == "Card":
        credits=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[normalize-space()='Buy an Amenify Gift Card'])[1]"))
            )
        credits.click()
        print("amenify gift card selected")
        time.sleep(2)
        credits=WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"(//input[@placeholder='Enter a value between $50 and $500*'])"))
            )
        credits.send_keys({amount})

        credits=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[contains(text(),'Buy Gift Card')])[1]"))
            )
        credits.click()
        print("credits bought")

    elif type == "Credits":
        credits=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Credits')]"))
            )
        credits.click()
        print("discounted credits box clicked")

        credits=WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH,"(//input[@placeholder='Enter a value between $50 and $500*'])"))
            )
        credits.send_keys({amount})

        credits=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[contains(text(),'Buy Credits')])[1]"))
            )
        credits.click()
        print("credits bought")
    else:
        print("No such survice")
            
        time.sleep(10)

    
def chores_popup_button(driver):
    time.sleep(2)
    try:
        standard= WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-146c3p1 r-fdjqy7 r-1ifxtd0 r-1un7vkp'])[1]"))
        )
        
        standard.click()
        
    except ElementClickInterceptedException:
        print("Element click intercepted by popup. Attempting to close popup...")

def corner_click(driver):
    # Use JavaScript to simulate a click at coordinates (0, 0)
    driver.execute_script("var evt = new MouseEvent('click', {clientX: 100, clientY: 100}); document.elementFromPoint(0, 0).dispatchEvent(evt);")
    

