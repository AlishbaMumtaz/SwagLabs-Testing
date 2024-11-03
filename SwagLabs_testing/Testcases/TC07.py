'''To test that the products are sorted alphabetically from Z to A.'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_filter_products_za():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        
        # Selecting "Name (Z to A)" from filter dropdown
        filter_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        filter_dropdown.select_by_visible_text("Name (Z to A)")
        time.sleep(2)

        # Capturing product names and verify sort order
        product_names = [item.text for item in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert product_names == sorted(product_names, reverse=True), "Products are not sorted Z to A."
        print("Test Passed: Products are sorted Z to A.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_filter_products_za()
