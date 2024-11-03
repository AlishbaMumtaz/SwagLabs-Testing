'''To test the logout button functionality of the sidebar'''

from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, 'C:\\Users\\HD\\SwagLabs_testing\\utility')
from webdriver_setup import initialize_driver


def test_logout_functionality():
    driver = initialize_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Log in with valid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Opening sidebar and clicking on "Logout"
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(2)

        # Verify redirection to login page
        assert driver.current_url == "https://www.saucedemo.com/", "Logout failed or redirection to login page failed."
        print("Test Passed: Logout button works correctly and redirects to login page.")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_logout_functionality()
