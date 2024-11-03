"""To test that clicking the Checkout button takes the user to the checkout information page."""

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_checkout_button_navigation():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Log in with valid credentials and add an item to cart
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Clicking on Checkout button
        driver.find_element(By.ID, "checkout").click()
        time.sleep(2)

        assert "Checkout: Your Information" in driver.page_source
        print("Test Passed: Navigated to checkout information page.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_checkout_button_navigation()
