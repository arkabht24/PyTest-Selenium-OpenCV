
import pytest

from compare_images import Screenshot_comparison
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


def pytest_runtest_setup(item):
    module_name = item.name
    baseline_output_dir = os.path.join(os.getcwd(), "Images","Baseline", f"{module_name}")
    actual_output_dir = os.path.join(os.getcwd(), "Images","Actual", f"{module_name}")
    comparison_output_dir = os.path.join(os.getcwd(), "Images","Comparison", f"{module_name}")
    
    os.makedirs(baseline_output_dir, exist_ok=True)
    os.makedirs(actual_output_dir, exist_ok=True)
    os.makedirs(comparison_output_dir, exist_ok=True)

    session = item.session

    session.baseline_output_dir = baseline_output_dir
    session.actual_output_dir = actual_output_dir
    session.comparison_output_dir = comparison_output_dir



# This hook runs before the tests are executed
# @pytest.hookimpl(tryfirst=True)
# def pytest_collection_modifyitems(session, config, items):
    
#     module_name = items[0].module.__name__.split(".")[-1]
    
#     baseline_output_dir = os.path.join(os.getcwd(), "Images","Baseline", f"{module_name}")
#     actual_output_dir = os.path.join(os.getcwd(), "Images","Actual", f"{module_name}")
#     comparison_output_dir = os.path.join(os.getcwd(), "Images","Comparison", f"{module_name}")
    
#     os.makedirs(baseline_output_dir, exist_ok=True)
#     os.makedirs(actual_output_dir, exist_ok=True)
#     os.makedirs(comparison_output_dir, exist_ok=True)

#     session.baseline_output_dir = baseline_output_dir
#     session.actual_output_dir = actual_output_dir
#     session.comparison_output_dir = comparison_output_dir

#     print(f"\nCreated directory for test artifacts: {output_dir}")



@pytest.fixture(scope="session")
def output_dir(request):
    return request.session.baseline_output_dir,request.session.actual_output_dir,request.session.comparison_output_dir

@pytest.fixture(scope = "session")
def visual_testing(request):
    return request.config.getoption("--visual-testing")



def pytest_runtest_teardown(item):
    module_name = item.name
    if item.config.getoption("--visual-testing") == 'yes':
        comparison = Screenshot_comparison()
        baseline_output_dir = os.path.join(os.getcwd(), "Images","Baseline", f"{module_name}")
        actual_output_dir = os.path.join(os.getcwd(), "Images","Actual", f"{module_name}")
        comparison_output_dir = os.path.join(os.getcwd(), "Images","Comparison", f"{module_name}")

        for image in os.listdir(baseline_output_dir):
            baseline_image = os.path.join(baseline_output_dir,image)
            actual_image = os.path.join(actual_output_dir,image)
            comparison_image = os.path.join(comparison_output_dir,image)
            comparison.compare_images_with_contours(baseline_image,actual_image,comparison_image)

