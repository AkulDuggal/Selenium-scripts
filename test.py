from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import random

from Functions import (
    initialize_driver,
    enter_info,
    click_service_by_text,
    corner_click
  
)

def random_click(driver):
    # Get the window size
    window_width = driver.execute_script("return window.innerWidth;")
    window_height = driver.execute_script("return window.innerHeight;")

    # Generate random x and y coordinates within the window bounds
    random_x = random.randint(0, window_width)
    random_y = random.randint(0, window_height)

    # Use JavaScript to simulate a click at the random coordinates
    driver.execute_script(f"var evt = new MouseEvent('click', {{clientX: {random_x}, clientY: {random_y}}}); document.elementFromPoint({random_x}, {random_y}).dispatchEvent(evt);")

def main():
    driver = initialize_driver('sign-in')



    try: 
        enter_info(driver, 'aduggal+nov1@amenify.com', 'Akulduggal46@123456')
        time.sleep(2)

        #HANDYMAN TESTING
        first_window=driver.current_window_handle
        time.sleep(2)
        click_service_by_text(driver,'Handyman')
        time.sleep(5)

        #random_click(driver)
        
        corner_click(driver)
        print("clicked at corner")
         
        time.sleep(2)
        #popup close
        '''handyman_start=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//button[@id='create-order-btn'])[1]"))
        )
        handyman_start.click()
        print("clicked ok button")
        time.sleep(1)'''


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


"""from Functions import (
    initialize_driver,
    enter_info,
    click_service_by_text,
    change_bedroom_bathroom,
    change_unit_number,
    click_next_button,
    choose_type,
    second_next_button_chores,
    selecting_chores,
    second_next_button,
    date_selection,
    checkout_button,
    promocode,
    final_button_chore,
    chores_popup_button,
    
    
)

def main():
    driver=initialize_driver('sign-in')
    try:
        enter_info(driver,'aduggal+gcp2@amenify.com', 'Akulduggal46@123456')
        click_service_by_text(driver,'Chores')
        change_unit_number(driver, '1')
        change_bedroom_bathroom(driver, 2, 3)
        click_next_button(driver)
        choose_type(driver,'single')
        time.sleep(2)
        chores_popup_button(driver) #this is not working, hence flow is incomplete
        second_next_button_chores(driver)
        selecting_chores(driver)
        second_next_button(driver)
        date_selection(driver, 30) #change according to the date to be selected 
        checkout_button(driver)
        promocode(driver,'OFF')
        final_button_chore(driver)
        

        # To be able to click the add instruction button 
        
        
        


        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()"""