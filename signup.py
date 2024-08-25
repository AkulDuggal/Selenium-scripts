import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

from Functions import (
    initialize_driver,
    enter_info
    
)

def main():
    driver = initialize_driver('sign-up')
    


    try: 
        enter_info(driver,'aduggal+fromvs@amenify.com','Akulduggal46@123456')
        time.sleep(2)
        
        input_fields = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "(//input[@placeholder=' '])"))
        )
        input_field_email = input_fields[2]
        input_field_email.clear()
        input_field_email.send_keys('Tester')
        input_field_email.send_keys(Keys.RETURN)

        input_field_password = input_fields[3]
        input_field_password.clear()
        input_field_password.send_keys(1)
        



        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        
        driver.quit()

if __name__ == "__main__":
    main()