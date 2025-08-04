from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="Chrome":
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        print("Chrome Browser Lanunched")
    elif browser=="Firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        print("Firefox Browser Lanunched")
    yield driver

# This will get value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")

# This will return the value of browser to setup method
@pytest.fixture()
def browser(request):  # ✅ fixture name should match the param in 'setup'
    return request.config.getoption("--browser")

#To generate pytest html report

# #It is a hook to adding environment info to HTML report
def pytest_configure(config):
    # Only add metadata if pytest-html plugin is active
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'PythonAutomationProjects'
        config._metadata['Module Name'] = 'Login'
        config._metadata['Tester'] = 'Sharmil'

# #It is a hook for delete/modify environment info to HTML report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)