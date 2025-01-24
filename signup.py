import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


from Utils.Functions import (
    initialize_driver,
    enter_info
    
)

def main():
    driver = initialize_driver('sign-up')

    try: 
        enter_info(driver,'aduggal+fromvs@amenify.com','Akulduggal46@123456')
        time.sleep(4)
        #this is working...IF BELOW WORKS, REMOVE THIS
        '''input_fields = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@placeholder,'')])[4]"))
        )
        input_fields.send_keys('Tester')
        input_fields.send_keys(Keys.RETURN)

        input_fields_unit = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@placeholder,'')])[5]"))
        )
        input_fields_unit.send_keys(1)'''

        input_fields = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@placeholder,'')]"))
        )
        print(f"Expected at least 5 input fields, but found {len(input_fields)}")
        input_fields[2].send_keys('Godrej') # THIS DOES NOT CLICK IT
        time.sleep(1)

        #CHECK
        #Work on this...choosing the property from dropdown box.
        option = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'css-175oi2r') and contains(., 'Godrej Icon (from, internal)')]"))
        )
        option.click()
    

        input_fields[2].send_keys(Keys.RETURN)
        time.sleep(2)
        input_fields[3].send_keys('Tester')
        input_fields[4].send_keys(1)


        #SELECT PARTNER FIELD
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//select[@data-testid='web_picker'])[1]"))
        )
        dropdown.click()
        dropdown.send_keys(Keys.ENTER)
       
        #HOW DID U HEAR ABOUT AMENIFY.
        dropdown_2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//select[@data-testid='web_picker'])[2]"))
        )

        select_dropdown = Select(dropdown_2)
        select_dropdown.select_by_index(3)        
        dropdown_2.click()
        dropdown_2.send_keys(Keys.ENTER)

        #CREATE BUTTON
        clicking=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[2]"))
        )
        clicking.click()


        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        
        driver.quit()

if __name__ == "__main__":
    main()