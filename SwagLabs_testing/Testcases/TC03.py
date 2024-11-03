'''
To test login with valid username and invalid password
'''

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_login_invalid_password():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("invalid_password")
        driver.find_element(By.ID, "login-button").click()
        
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert "Epic sadface" in error_message, "Expected error message not displayed."
        print("Test Passed: Login with valid username and invalid password shows error message.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_login_invalid_password()
