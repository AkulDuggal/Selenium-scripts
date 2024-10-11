from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from Functions import (
    initialize_driver,
    enter_info,
    #click_cleaning_service,
    change_bedroom_bathroom,
    change_unit_number,
    click_next_button,
    click_skip_button,
    service_selection,
    second_next_button,
    click_service_by_text,
    click_element_by_xpath,
    choose_type,
    next_button_for_cleaning1,
    date_selection,
    final_button_chore,
    add_ons,
    final_next_cleaning,
    promocode,
    final_button_cleaning
    
    
)

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver, 'aduggal@amenify.com', 'Akulduggal46@123456')
        time.sleep(1)
        click_service_by_text(driver,'Cleaning')
        time.sleep(2)
        change_unit_number(driver, '3')
        change_bedroom_bathroom(driver, 1, 1)
        click_next_button(driver)
        click_skip_button(driver)
        service_selection(driver)
        second_next_button(driver)
        choose_type(driver,'single')
        next_button_for_cleaning1(driver)
        date_selection(driver, 30)
        time.sleep(3)
        final_button_chore(driver) #change name to a commonn name.
        add_ons(driver)
        final_next_cleaning(driver)
        #FINAL CHECKOUT SCREEN
        promocode(driver,'OFF')
        #final_button_cleaning(driver)

        time.sleep(2)
        done=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[18]"))
        )
        done.click()
        print("Cleaning flow complete")







        

        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

