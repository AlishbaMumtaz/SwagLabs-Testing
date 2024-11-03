"""To test that product images load correctly for all items on the product page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_product_image_visibility():
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

        # Verifying that product images are visible
        product_images = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_img")))
        for img in product_images:
            assert img.is_displayed(), "Product image is not visible."

        print("Test Passed: All product images are displayed correctly.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_product_image_visibility()
