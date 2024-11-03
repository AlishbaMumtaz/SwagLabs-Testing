'''To verify that the cart icon shows the correct number of items'''

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_cart_icon_count():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in and add items
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Adding items to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)

        # Verifying cart icon count is 2
        cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_count == "2", "Cart icon count is incorrect."
        print("Test Passed: Cart icon count is correct.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_cart_icon_count()
