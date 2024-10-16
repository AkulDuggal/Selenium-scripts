#DIVIDE CLEANING/CHORES FUNCTION FOR READABILITY. 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

def click_service_by_text(driver, service_text):
    try:
        service = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[normalize-space()='{service_text}']"))
        )
        service.click()
        print(f"'{service_text}' service clicked successfully")
    except Exception as e:
        print(f"Failed to click the '{service_text}' service")


def change_unit_number(driver, unit_number):
    unit_number_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='text-input-flat']"))
    )
    unit_number_field.click()
    unit_number_field.send_keys(Keys.CONTROL + "a")  
    unit_number_field.send_keys(unit_number)

def change_bedroom_bathroom(driver, num_bedrooms, num_bathrooms):
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//select[@data-testid='web_picker']"))
    )
    select_bedroom = Select(dropdown[0])
    select_bedroom.select_by_visible_text(f'{num_bedrooms} bed(s)')

    select_bathroom = Select(dropdown[1])
    select_bathroom.select_by_visible_text(f'{num_bathrooms} bath(s)')

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
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[10]"))
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
        driver.quit() #might need to remove this

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


def final_button_chore(driver):
    done=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[14]"))
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
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[10]"))
    )
    time.sleep(1)
    standard.click()
    print("Clicked next button from the second function")


def next_button_for_cleaning1(driver):
    time.sleep(2)
    standard= WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[12]"))
    )
    time.sleep(1)
    standard.click()


def final_next_cleaning(driver):
    standard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[16]"))
        )
    standard.click() 
    time.sleep(1)
    print("Clicked next button")


def final_button_cleaning(driver):
    done=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[18]"))
    )
    done.click()
    time.sleep(5)
    print("Cleaning flow complete")


