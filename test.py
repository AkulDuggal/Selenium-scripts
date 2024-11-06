from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from Functions import (
    initialize_driver,
    enter_info,
    click_service_by_text
    
    
    
)

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver, 'aduggal+nov1@amenify.com', 'Akulduggal46@123456')
        time.sleep(2)

        #HANDYMAN TESTING
        first_window=driver.current_window_handle
        click_service_by_text(driver,'Handyman')
        time.sleep(4)
        

        #popup close
        handyman_start=WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH,"(//div[@class='swal-button-container'])[1]"))
        )
        handyman_start.click()
        print("clicked ok button")
        time.sleep(1)


        #date selection
        date_select=WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,"(//input[@id='dpDate'])[1]"))
        )
        date_select.click()
        time.sleep(1)

        dates=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//a[normalize-space()='27'])[1]"))
        )
        dates.click()
        print("date selected")




        #driver.switch_to.window(first_window)


        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

