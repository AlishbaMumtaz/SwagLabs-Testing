from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def initialize_driver():
    # Creating a Service object for ChromeDriver using WebDriverManager
    service = Service(ChromeDriverManager().install())
    
    # Initializing the Chrome WebDriver
    driver = webdriver.Chrome(service=service)
    
    return driver
