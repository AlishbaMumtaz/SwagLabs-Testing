'''To verify that the user can return to the product page and add more items'''

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_continue_shopping():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Adding an item and continue shopping
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        driver.find_element(By.ID, "continue-shopping").click()
        time.sleep(1)

        
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)

        # Verify cart count
        cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_count == "2", "Failed to add more items after continuing shopping."
        print("Test Passed: User can continue shopping and add more items.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_continue_shopping()
