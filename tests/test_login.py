import pytest


from pages import login_page
from utils.config_reader import PASSWORD, USERNAME



def test_login_for_user(driver,output_dir):
    login_page_obj = login_page.Login_page(driver,output_dir)
    login_page_obj.navigate_to_login_page()
    login_page_obj.login(USERNAME,PASSWORD)