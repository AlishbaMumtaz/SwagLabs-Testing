'''To verify that the user cannot add more than one quantity of the same item'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_add_same_item_twice():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Wait for and add an item to the cart
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_button.click()

        # Wait for the button to change to "Remove" after adding
        remove_button = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "remove-sauce-labs-backpack"), "Remove")
        )
        
        # Verify that "Add to Cart" button is no longer available for the same item
        assert remove_button, "Add to Cart button still available after adding the item."
        print("Test Passed: Cannot add more than one quantity of the same item.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_add_same_item_twice()
