import time
from Functions import (
    initialize_driver,
    sign_in,
    click_cleaning_service,
    change_bedroom_bathroom,
    change_unit_number,
    click_next_button,
    click_skip_button,
    service_selection,
    second_next_button
)

def main():
    driver = initialize_driver()

    try: #standard cleaning flow
        sign_in(driver, 'aduggal@amenify.com', 'Akulduggal46@123456')
        time.sleep(1)
        click_cleaning_service(driver)
        time.sleep(2)
        change_bedroom_bathroom(driver, 1, 1)
        change_unit_number(driver, '3')
        click_next_button(driver)
        click_skip_button(driver)
        service_selection(driver)
        second_next_button(driver)



        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
