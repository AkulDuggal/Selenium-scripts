from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from Functions import (
    initialize_driver,
    enter_info,
    
    
)

def main():
    driver = initialize_driver('sign-in')

    try: 
        enter_info(driver, 'aduggal@amenify.com', 'Akulduggal46@123456')
        time.sleep(5)

        #GO TO SETTINGS PAGE
        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//button[@role='button'])[4]"))
        ).click()
        print("settings button clicked")



        #SELECT FIRST SETTING
        #(//div[@class='css-175oi2r r-1awozwy r-18u37iz']) IS THE COMMON FOR ALL SETTINGS.
        settings_one=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1awozwy r-18u37iz'])[1]"))
        ).click()
        print("first setting clicked")
        time.sleep(2)

        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty r-13qz1uu'])[1]"))
        ).click()
        print("settings updated")

        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-146c3p1 r-lrvibr r-1loqt21'])[1]"))
        ).click()
        print("Back to settings")

        #second setting
        settings_2=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1awozwy r-18u37iz'])[2]"))
        ).click()
        print("Second setting clicked")
        time.sleep(2)

        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty r-13qz1uu'])[1]"))
        ).click()
        print("settings updated")

        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-146c3p1 r-lrvibr r-1loqt21'])[1]"))
        ).click()
        print("Back to settings")

        #3rd setting , clicking this increases the count in array
        settings_2=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1awozwy r-18u37iz'])[3]"))
        ).click()
        print("third setting clicked")
        time.sleep(2)







        time.sleep(10)
    

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

