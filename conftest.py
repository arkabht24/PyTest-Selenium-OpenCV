
import pytest
from utils.get_drivers import get_driver
import os
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome", help = "Browser to use: chrome/firefox")
    parser.addoption("--visual-testing", action = "store", default = "no", help = "Visual Testing: yes or no")
    

@pytest.fixture(scope = "function")
def driver(request):
    browser = request.config.getoption("browser")
    driver = get_driver(browser)
    yield driver
    driver.quit()




# This hook runs before the tests are executed
@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(session, config, items):
    
    # Get the module name from the first collected test item
    module_name = items[0].module.__name__.split(".")[-1]
    
    baseline_output_dir = os.path.join(os.getcwd(), "Images","Baseline", f"{module_name}")
    actual_output_dir = os.path.join(os.getcwd(), "Images","Actual", f"{module_name}")
    comparison_output_dir = os.path.join(os.getcwd(), "Images","Comparison", f"{module_name}")
    
    os.makedirs(baseline_output_dir, exist_ok=True)
    os.makedirs(actual_output_dir, exist_ok=True)
    os.makedirs(comparison_output_dir, exist_ok=True)

    session.baseline_output_dir = baseline_output_dir
    session.actual_output_dir = actual_output_dir
    session.comparison_output_dir = comparison_output_dir

    print(f"\nCreated directory for test artifacts: {output_dir}")



@pytest.fixture(scope="session")
def output_dir(request):
    return request.session.baseline_output_dir,request.session.actual_output_dir,request.session.comparison_output_dir

@pytest.fixture(scope = "session")
def visual_testing(request):
    return request.config.getoption("--visual-testing")