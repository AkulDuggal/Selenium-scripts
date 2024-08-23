import time
from Functions import (
    initialize_driver,
    sign_in,
    click_service_by_text,
    change_bedroom_bathroom,
    change_unit_number,
    click_next_button
)

def main():
    driver=initialize_driver()
    try:
        sign_in(driver,'aduggal@amenify.com', 'Akulduggal46@123456')
        click_service_by_text(driver,'Chores')
        change_unit_number(driver, '1')
        change_bedroom_bathroom(driver, 2, 3)
        click_next_button(driver)


        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()



