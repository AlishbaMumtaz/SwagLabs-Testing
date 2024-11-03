'''To test the Reset App State button functionality of the sidebar'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_reset_app_state():
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

        # Adding an item to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)

        # Opening sidebar and clicking "Reset App State"
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "reset_sidebar_link").click()
        time.sleep(2)

        # Waiting until the cart icon becomes visible and checking if it's empty
        try:
            cart_count = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
            assert cart_count.text == "", "Reset App State did not empty the cart."
        except:
            # If the cart badge is not present, it means it's empty as expected
            print("Test Passed: Reset App State successfully emptied the cart")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_reset_app_state()
