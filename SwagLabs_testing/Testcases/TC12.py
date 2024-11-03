'''To verify that clicking on an item displays the correct description'''
from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_view_item_description():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Clicking on an item to view its description
        driver.find_element(By.ID, "item_4_title_link").click()
        time.sleep(2)

        # Verifying description page loaded
        item_name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
        item_description = driver.find_element(By.CLASS_NAME, "inventory_details_desc").text
        assert "Sauce Labs Backpack" in item_name, "Item description not displayed correctly."
        
        # Printing the item name and description text
        print(f"Test Passed: {item_name} description displayed correctly.")
        print("Description Text:")
        print(item_description)

        # Taking a screenshot of the description page
        screenshot_path = "item_description_screenshot.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_view_item_description()
