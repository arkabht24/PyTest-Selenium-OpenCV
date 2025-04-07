

import os
import time
from utils import locator_loader
from utils.config_reader import BASE_URL


class Login_page:
    def __init__(self,driver):
        self.driver = driver
        locator_path = str(os.path.join(os.getcwd(),"locators","login_locators.json"))
        print("Locator path ---> ",locator_path)
        self.locators = locator_loader.load_locators(locator_path)

    def navigate_to_login_page(self):
        self.driver.get(BASE_URL)
        time.sleep(5)

    def input_username(self,username):
        print("Locator of username ---> ",*self.locators["USERNAME_INPUT"])
        self.driver.find_element(*self.locators["USERNAME_INPUT"]).send_keys(username)
        time.sleep(5)

    def input_password(self,password):
        print("Locator of password ---> ",*self.locators["PASSWORD_INPUT"])
        self.driver.find_element(*self.locators["PASSWORD_INPUT"]).send_keys(password)
        time.sleep(5)

    def click_on_login_button(self):
        self.driver.find_element(*self.locators["LOGIN_BUTTON"]).click()
        time.sleep(5)

    def login(self,username,password):
        self.input_username(username)
        self.input_password(password)
        self.click_on_login_button()