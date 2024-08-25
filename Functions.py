from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

def initialize_driver(access_type):
    driver = webdriver.Chrome()
    if access_type=='sign-up':
        driver.get('https://m.joinamenify.com/sign-up')
    elif access_type=='sign-in':
        driver.get('https://m.joinamenify.com/sign-in')
    else:
        driver.quit()
    return driver

def enter_info(driver, email, password):
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
        EC.presence_of_element_located((By.XPATH, "//div[@class='css-175oi2r r-1phboty']"))
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
    driver.execute_script("arguments[0].value = '';", unit_number_field) #the unit number does not get cleared...check later
    unit_number_field.clear()
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
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[10]"))
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
