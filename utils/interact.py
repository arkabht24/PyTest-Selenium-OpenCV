
class Interact:

    def __init__(self,driver):
        self.driver = driver

    def click_webelement(self,element):
        self.scroll_to_center(element)
        element.click()
    
    def scroll_to_center(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'})",element)

    def take_screenshot(self,screenshot_full_file_path_with_name):
        self.driver.save_screenshot(screenshot_full_file_path_with_name)
