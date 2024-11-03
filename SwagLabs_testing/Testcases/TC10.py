'''To verify that the selected item is successfully added to the cart'''

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_add_item_to_cart():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Adding an item to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)

        # Verifying item count in cart icon
        cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_count == "1", "Item not successfully added to cart."
        print("Test Passed: Item successfully added to cart.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_add_item_to_cart()
