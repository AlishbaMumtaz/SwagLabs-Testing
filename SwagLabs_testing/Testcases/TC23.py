"""To test that clicking the Finish button completes the order and shows the confirmation page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_finish_purchase():
    driver = initialize_driver()
    wait = WebDriverWait(driver, 10)  

    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Adding an item to the cart
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

       
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # Entering user information 
        wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Alishba")
        driver.find_element(By.ID, "last-name").send_keys("Tester")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

        # Verifying the presence of the confirmation message
        confirmation_message = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Thank you for your order!']"))
        )
        assert confirmation_message.is_displayed(), "Order confirmation message not displayed."
        print("Test Passed: Order confirmation displayed.")

    except Exception as e:
        print(f"Test Failed: {e}")

    finally:
        driver.quit()

test_finish_purchase()
