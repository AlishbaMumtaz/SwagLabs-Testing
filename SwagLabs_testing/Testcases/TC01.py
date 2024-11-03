'''
To test login with valid username and password
'''

from selenium.webdriver.common.by import By
import time
import sys

# Adding the utility folder to the system path
sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')


# Importing the initialize_driver function from webdriver_setup
from webdriver_setup import initialize_driver

def test_login():
    # Initializing the WebDriver
    driver = initialize_driver()
    
    try:
        # Navigating to the login page
        driver.get("https://www.saucedemo.com/")
       
        driver.maximize_window()

        username_field = driver.find_element(By.ID, "user-name").send_keys("standard_user")
        
     
        password_field = driver.find_element(By.ID, "password").send_keys("secret_sauce")
       
        login_button = driver.find_element(By.ID, "login-button").click()
        
        time.sleep(3)
     
        assert "https://www.saucedemo.com/inventory.html" in driver.current_url, "Login failed!"
        print("Test Passed: Login with valid credentials successful.")
    
    except Exception as e:
        print(f"Test Failed: {e}")
    
    finally:
        driver.quit()

# Run the test
test_login()
