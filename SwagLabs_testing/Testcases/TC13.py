'''To verify that an item can be removed from the cart'''

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_remove_item_from_cart():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Adding and then removing an item from the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(1)

        # Verifying cart icon count is removed
        cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert not cart_badge, "Cart is not empty after removing item."
        print("Test Passed: Item successfully removed from the cart.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_remove_item_from_cart()
