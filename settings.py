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
        '''settings_one=WebDriverWait(driver,10).until(
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
        time.sleep(5)

        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-146c3p1 r-lrvibr r-1loqt21'])[1]"))
        ).click()
        print("Back to settings")'''

        #3rd setting , clicking this increases the count in array
        '''settings_2=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1awozwy r-18u37iz'])[3]"))
        )
        settings_2.click()
        print("third setting clicked")
        settings_2.click()
        time.sleep(2)
        
        settings_2=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1awozwy r-18u37iz'])[4]"))
        )
    
        settings_2.click()
        print("Fourth setting clicked")
        settings_2.click()

        settings_2=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1awozwy r-18u37iz'])[3]"))
        )'''

        all_elements=WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.XPATH,"(//div[@class='css-175oi2r r-1awozwy r-18u37iz'])"))
        )
        # the code below is working, need to find a way to click "success" message or avoid it to let the flow continue.
        '''all_elements[0].click()

        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty r-13qz1uu'])[1]"))
        ).click()
        print("settings updated")
        time.sleep(3)

        settings=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"(//div[@class='css-175oi2r'])[93]"))
        ).click()
        

        time.sleep(2)

        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-146c3p1 r-lrvibr r-1loqt21'])[1]"))
        ).click()
        print("Back to settings")

        all_elements[1].click()
        
        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty r-13qz1uu'])[1]"))
        ).click()
        print("settings updated")
        time.sleep(4)

        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-146c3p1 r-lrvibr r-1loqt21'])[1]"))
        ).click()
        print("Back to settings")
        time.sleep(4)'''


        all_elements[2].click()
        print("clicked 3rd setting")
        time.sleep(2)
        all_elements[2].click()

        all_elements[3].click()
        print("clicked 4th setting")
        time.sleep(3)
        all_elements[3].click()

        all_elements[4].click()
        print("clicked 5th setting")
        time.sleep(3)
        all_elements[4].click()



        time.sleep(10)
    

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

