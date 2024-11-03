'''To test that the products are sorted alphabetically from A to Z'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_filter_products_az():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Waiting for inventory page to load
        WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

        # Selecting "Name (A to Z)" from filter dropdown
        filter_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        filter_dropdown.select_by_visible_text("Name (A to Z)")
        
        # Waiting for products to sort
        time.sleep(2)  # Alternatively, use WebDriverWait for a specific element if necessary

        # Capture product names and verify sort order
        product_names = [item.text for item in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert product_names == sorted(product_names), f"Products are not sorted A to Z: {product_names}"
        print("Test Passed: Products are sorted A to Z.")
        
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_filter_products_az()



