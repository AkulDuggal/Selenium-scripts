import time
from Functions import (
    initialize_driver,
    enter_info
    
)

def main():
    driver = initialize_driver('sign-up')
    


    try: 
        enter_info(driver,'aduggal+fromvs@amenify.com','Akulduggal46@123456')
        
        



        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        
        driver.quit()

if __name__ == "__main__":
    main()