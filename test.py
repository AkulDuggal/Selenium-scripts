def random_click(driver):
    # Get the window size
    window_width = driver.execute_script("return window.innerWidth;")
    window_height = driver.execute_script("return window.innerHeight;")

    # Generate random x and y coordinates within the window bounds
    random_x = random.randint(0, window_width)
    random_y = random.randint(0, window_height)

    # Use JavaScript to simulate a click at the random coordinates
    driver.execute_script(f"var evt = new MouseEvent('click', {{clientX: {random_x}, clientY: {random_y}}}); document.elementFromPoint({random_x}, {random_y}).dispatchEvent(evt);")

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.cleaning.cleaning_functions import(
    initialize_driver,
    enter_info,
    click_service_by_text,
    change_bedroom_bathroom,
    change_unit_number,
    click_next_button,
    click_skip_button,
    service_selection,
    second_next_button,
    choose_type,
    cleaning_popup_button,
    next_button_for_cleaning1,
    date_selection,
    last_next_button,
    add_ons,
    checkout,
    pro_tip,
    submit,
    check
)

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver)
        time.sleep(6)
        click_service_by_text(driver,'Cleaning')
        time.sleep(1)
        change_bedroom_bathroom(driver, 1, 1)
        change_unit_number(driver, '4')
        time.sleep(2)
        click_next_button(driver)
        time.sleep(2)
        click_skip_button(driver)
        time.sleep(2)
        service_selection(driver,"Standard")
        time.sleep(2)
        second_next_button(driver)
        time.sleep(2)
        choose_type(driver,'single')  
        time.sleep(2)
        cleaning_popup_button(driver) # ADD THIS TO THE ABOVE FUNCTION LATER
        time.sleep(2)
        next_button_for_cleaning1(driver)
        time.sleep(2)

        #WORK ON THIS ...SEE GPT
        data_testid = "undefined.day_2025-01-31"
        date_element_aria_label = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@data-testid='{data_testid}']")))
        date_element_aria_label.click()

        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()