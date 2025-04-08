
import pytest
from utils.get_drivers import get_driver
import os
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome", help = "Browser to use: chrome/firefox")
    

@pytest.fixture(scope = "function")
def driver(request):
    browser = request.config.getoption("browser")
    driver = get_driver(browser)
    yield driver
    driver.quit()




# This hook runs before the tests are executed
@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(session, config, items):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Get the module name from the first collected test item
    module_name = items[0].module.__name__.split(".")[-1]
    
    output_dir = os.path.join(os.getcwd(), "Images", f"{module_name}_{timestamp}")
    print("Images directory ---> ", output_dir)
    os.makedirs(output_dir, exist_ok=True)

    session.output_dir = output_dir

    print(f"\nCreated directory for test artifacts: {output_dir}")


@pytest.fixture(scope="session")
def output_dir(request):
    return request.session.output_dir
