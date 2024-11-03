'''To test filter products by price low to high functionality'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_filter_products_price_low_to_high():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        
        # Selecting "Price (low to high)" from filter dropdown
        filter_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        filter_dropdown.select_by_visible_text("Price (low to high)")
        time.sleep(2)

        # Capture product prices and verify sort order
        product_prices = [float(item.text.replace("$", "")) for item in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        assert product_prices == sorted(product_prices), "Products are not sorted by price low to high."
        print("Test Passed: Products are sorted by price low to high.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_filter_products_price_low_to_high()