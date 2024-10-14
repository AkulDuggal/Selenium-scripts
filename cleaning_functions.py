#DIVIDE CLEANING/CHORES FUNCTION FOR READABILITY. 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

def click_skip_button(driver):
    next_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Skip')]"))
    )
    next_button.click()
    print("Moved to next page, from skip click function")


def service_selection(driver):
    standard = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[normalize-space()='Standard'])[1]"))
    )
    standard.click()
    print("Clicked standard service")



def second_next_button(driver): 
    time.sleep(1)   
    standard = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[10]"))
    )
    time.sleep(1)
    standard.click()
    print("Clicked next button from the second function")


def next_button_for_cleaning1(driver):
    time.sleep(2)
    standard= WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[12]"))
    )
    time.sleep(1)
    standard.click()


def final_next_cleaning(driver):
    standard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='css-175oi2r r-1phboty'])[16]"))
        )
    standard.click() 
    time.sleep(1)
    print("Clicked next button")


def final_button_cleaning(driver):
    done=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='css-175oi2r r-1phboty'])[18]"))
    )
    done.click()
    time.sleep(5)
    print("Cleaning flow complete")


