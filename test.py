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







        

        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

