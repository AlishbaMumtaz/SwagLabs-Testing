'''To test the about button functionality of the sidebar'''

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver

def test_about_button_navigation():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Logging in with valid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Opening sidebar and clicking "About"
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "about_sidebar_link").click()
        time.sleep(2)

        # Verify the current URL to confirm navigation
        assert "saucelabs.com" in driver.current_url, "Navigation to About page failed."
        print("Test Passed: About button navigates to the correct page.")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_about_button_navigation()
