
import pytest
from utils.get_drivers import get_driver


def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome", help = "Browser to use: chrome/firefox")
    

@pytest.fixture(scope = "function")
def driver(request):
    browser = request.config.getoption("browser")
    driver = get_driver(browser)
    yield driver
    driver.quit()