import json
from selenium.webdriver.common.by import By

# Map locator strategy string to Selenium By
BY_MAP = {
    "id": By.ID,
    "name": By.NAME,
    "xpath": By.XPATH,
    "css": By.CSS_SELECTOR,
    "class": By.CLASS_NAME,
    "link_text": By.LINK_TEXT,
    "partial_link_text": By.PARTIAL_LINK_TEXT,
    "tag": By.TAG_NAME
}

def load_locators(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    
    return {
        key: (BY_MAP[value[0].lower()], value[1]) for key, value in data.items()
    }
