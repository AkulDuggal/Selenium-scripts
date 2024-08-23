from time import time
from selenium import webdriver

# Replace with the path to your WebDriver executable
driver = webdriver.Chrome()

driver.get("m.joinamenify.com")
time.sleep(5)

driver.quit()
