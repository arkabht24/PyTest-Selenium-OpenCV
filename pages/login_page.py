

import os
import shutil
import time
from utils import interact, locator_loader
from utils.config_reader import BASE_URL

def clean_directory_completely(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  
                print(f"Deleted file: {file_path}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  
                print(f"Deleted folder: {file_path}")
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

class Login_page:

    def __init__(self,driver,output_dir,visual_testing):
        self.visual_testing = visual_testing
        self.driver = driver
        self.baseline_dir_path,self.actual_dir_path,self.comparison_dir_path = output_dir

        if visual_testing == 'no':
            clean_directory_completely(self.baseline_dir_path)
        else:
            clean_directory_completely(self.actual_dir_path)
            clean_directory_completely(self.comparison_dir_path)
    
        self.interact = interact.Interact(driver)
        locator_path = str(os.path.join(os.getcwd(),"locators","login_locators.json"))
        print("Locator path ---> ",locator_path)
        self.locators = locator_loader.load_locators(locator_path)

    def navigate_to_login_page(self):
        self.driver.get(BASE_URL)
        time.sleep(5)
        dir_path = self.baseline_dir_path
        if self.visual_testing == 'yes':
            dir_path = self.actual_dir_path
        self.interact.take_screenshot(os.path.join((dir_path),"Navigated to application.png"))


    def input_username(self,username):
        print("Locator of username ---> ",*self.locators["USERNAME_INPUT"])
        self.driver.find_element(*self.locators["USERNAME_INPUT"]).send_keys(username)
        time.sleep(5)
        dir_path = self.baseline_dir_path
        if self.visual_testing == 'yes':
            dir_path = self.actual_dir_path
        self.interact.take_screenshot(os.path.join((dir_path),"Username inserted.png"))

    def input_password(self,password):
        print("Locator of password ---> ",*self.locators["PASSWORD_INPUT"])
        self.driver.find_element(*self.locators["PASSWORD_INPUT"]).send_keys(password)
        time.sleep(5)
        dir_path = self.baseline_dir_path
        if self.visual_testing == 'yes':
            dir_path = self.actual_dir_path
        self.interact.take_screenshot(os.path.join((dir_path),"Password inserted.png"))

    def click_on_login_button(self):
        self.driver.find_element(*self.locators["LOGIN_BUTTON"]).click()
        time.sleep(5)
        dir_path = self.baseline_dir_path
        if self.visual_testing == 'yes':
            dir_path = self.actual_dir_path
        self.interact.take_screenshot(os.path.join((dir_path),"Clicked on Login Button and logged in.png"))

    def login(self,username,password):
        self.input_username(username)
        self.input_password(password)
        # self.click_on_login_button()