"""To test that clicking the Back Home button on the confirmation page redirects the user to the product page."""

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_back_to_home_button():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Log in, add item, proceed through checkout, and complete order
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        time.sleep(2)

        # Entering user information 
        driver.find_element(By.ID, "first-name").send_keys("Alishba")
        driver.find_element(By.ID, "last-name").send_keys("Tester")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        # Finish purchase
        driver.find_element(By.ID, "finish").click()
        time.sleep(2)

       
        driver.find_element(By.ID, "back-to-products").click()
        time.sleep(2)

        assert "Products" in driver.page_source
        print("Test Passed: User successfully redirected to product page.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_back_to_home_button()
