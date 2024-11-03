"""To test that entering valid information and continuing takes the user to the order overview page."""

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_continue_with_user_info():
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

        # Filling info
        driver.find_element(By.ID, "first-name").send_keys("Alishba")
        driver.find_element(By.ID, "last-name").send_keys("Mumtaz")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        assert "Checkout: Overview" in driver.page_source
        print("Test Passed: Navigated to order overview page.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_continue_with_user_info()
