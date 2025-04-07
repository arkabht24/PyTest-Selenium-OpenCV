import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def get_driver(browser="chrome"):
    """
    Function to initialize WebDriver based on the browser argument.
    Uses locally stored drivers for Chrome and Firefox.
    Default is Chrome.
    """
    # Get the path to the drivers in your project directory
    chromedriver_path = os.path.join(os.getcwd(), 'drivers', 'chromedriver')
    geckodriver_path = os.path.join(os.getcwd(), 'drivers', 'geckodriver')

    if browser.lower() == "chrome":
        # Setting Chrome options
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # Optional: Start browser maximized
        chrome_options.add_argument("--disable-extensions")  # Optional: Disable extensions
        # Point to the local ChromeDriver path
        driver = webdriver.Chrome(service=ChromeService(chromedriver_path), options=chrome_options)

    elif browser.lower() == "firefox":
        # Setting Firefox options
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")  # Optional: Start browser maximized
        # Point to the local GeckoDriver path
        driver = webdriver.Firefox(service=FirefoxService(geckodriver_path), options=firefox_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    return driver
