"""To test that clicking the Cancel button during checkout returns the user to the cart page."""

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_cancel_button_during_checkout():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Log in, add item, and proceed to checkout
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        time.sleep(2)

       
        driver.find_element(By.ID, "cancel").click()
        time.sleep(2)

        assert "Your Cart" in driver.page_source
        print("Test Passed: User returned to the cart page.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_cancel_button_during_checkout()