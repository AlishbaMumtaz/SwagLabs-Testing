"""To test that an error message is displayed when the user tries to continue without filling required fields."""

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_continue_without_user_info():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Log in, add item, and proceed to checkout information page
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        time.sleep(2)

        # Attempt to continue without filling information
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Error: First Name is required" in error_message
        print("Test Passed: Error message displayed for missing information.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_continue_without_user_info()
