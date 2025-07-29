#This file contains all the functions for settings flow .
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

def settings(driver):
    settings=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//button[@role='button'])[4]"))
    ).click()
    print("settings button clicked")

def setting_one(driver):
    time.sleep(2)
    setting_button = driver.find_element(By.XPATH, "//div[text()='Personal information']")
    driver.execute_script("arguments[0].click();", setting_button)

    print("first setting clicked")
    time.sleep(2)

    settings=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//div[text()='Update']"))
        )
    settings.click()
    print("settings updated")

    settings=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-146c3p1 r-lrvibr r-1loqt21'])[1]"))
        ).click()
    print("Back to settings")

    
def setting_two(driver):
        setting_button = driver.find_element(By.XPATH, "//div[text()='My Property / Address']")
        driver.execute_script("arguments[0].click();", setting_button)
        print("Second setting clicked")
        time.sleep(2)

        settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//div[text()='Update']"))
            )
        settings.click()
        print("settings updated")
        time.sleep(2)
        
        #IF THE ABOVE BUTTON IS CLICKED, THIS CODE IS NOT REQUIRED. Add assertion here
        ''' settings=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-146c3p1 r-lrvibr r-1loqt21'])[1]"))
        ).click()
        print("Back to settings")'''


def third_setting(driver):
    setting_button = driver.find_element(By.XPATH, "//div[text()='Payment']")
    driver.execute_script("arguments[0].click();", setting_button)
    print("payment option opened ")
    time.sleep(2)


    setting_button = driver.find_element(By.XPATH, "//div[text()='Payment']")
    driver.execute_script("arguments[0].click();", setting_button)
    print("payment option closed")
    time.sleep(2)



#try this later, allows the whole page to be accessed under a single xpath
def settings_common(driver):
    all_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "(//div[contains(@class, 'css-175oi2r') and @tabindex='0'])"))
        )

# Ensure the third element exists and is clickable
    if len(all_elements) > 2:
        test=WebDriverWait(driver, 10).until(EC.element_to_be_clickable(all_elements[2]))
        test.click()
        print("clicked the third element")
    else:
        print("Less than 3 elements found!")



def fourth_setting(driver):
    setting_button = driver.find_element(By.XPATH, "//div[text()='Amenify wallet']")
    driver.execute_script("arguments[0].click();", setting_button)
    print("payment option opened ")
    time.sleep(2)

    setting_button = driver.find_element(By.XPATH, "//div[contains(text(),'View Wallet History')]")
    driver.execute_script("arguments[0].click();", setting_button)
    print("Can see the wallet credits")
    
    wallet = driver.find_element(By.XPATH, "//div[text()='Amenify wallet']")
    driver.execute_script("arguments[0].click();", wallet)
    print("in the wallet page")
    time.sleep(3)


    settings=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1i6wzkk r-lrvibr r-1loqt21 r-1otgn73 r-1awozwy r-is05cd'])[1]"))
        )
    settings.click()
    print("back to settings")
    time.sleep(2)

def fifth_setting(driver):
    setting_button = driver.find_element(By.XPATH, "//div[text()='Notifications']")
    driver.execute_script("arguments[0].click();", setting_button)
    print("Notification opened")
    time.sleep(2)

    switch=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//input[@role='switch'])[1]"))
    )
    switch.click()
    print("clicked")
    time.sleep(1)
    switch.click()

    switch=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//input[@role='switch'])[2]"))
    )
    switch.click()
    time.sleep(2)
    #find a case where the popup needs to be clicked, otherwise avoid
    '''okay_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='button']"))
        )
    okay_button.click()
    print("Closed popup")'''

def sixth_setting(driver):
    setting_button = driver.find_element(By.XPATH, "//div[text()='Amenify Bundle Subscription']")
    driver.execute_script("arguments[0].click();", setting_button)

    print("clicked amenify bundle membership")

def seventh_setting(driver):
    setting_button = driver.find_element(By.XPATH, "//div[text()='Unsubscribe a service']")
    driver.execute_script("arguments[0].click();", setting_button)

    print("clicked unsub button")

def eigth_setting(driver):
    setting_button = driver.find_element(By.XPATH, "//div[text()='Property Manager Activation']")
    driver.execute_script("arguments[0].click();", setting_button)

    print("clicked property manager button")

def nineth_setting(driver):
    setting_button = driver.find_element(By.XPATH, "//div[text()='Redeem Credits']")
    driver.execute_script("arguments[0].click();", setting_button)

    print("clicked redeem credit button")


# this is working, make it a common class later, maybe create a json file in this folder and add text from there
def common_class(driver,text):
    setting_button = driver.find_element(By.XPATH, f"//div[text()='{text}']")
    driver.execute_script("arguments[0].click();", setting_button)

    print(f"clicked {text} button")
