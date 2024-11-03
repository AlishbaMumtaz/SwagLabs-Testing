"""To test that the total price displayed in the cart is accurate based on the items added."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_total_price_calculation():
    driver = initialize_driver()
    wait = WebDriverWait(driver, 10)  
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Adding items to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        # Click on Checkout to proceed to the information page
        driver.find_element(By.ID, "checkout").click()
        time.sleep(2)

        
        driver.find_element(By.ID, "first-name").send_keys("Alishba")
        driver.find_element(By.ID, "last-name").send_keys("Tester")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        # Calculating total price of added items
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        total_price = sum(float(price.text.replace("$", "")) for price in prices)
        
        displayed_total = float(driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text.split("$")[1])
        
        assert displayed_total == total_price, "Total price displayed in the cart is incorrect."
        print("Test Passed: Total price calculated correctly in the cart.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_total_price_calculation()
