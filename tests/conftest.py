import pytest
from selenium import webdriver


def pytest_addoption(parser):
    # telling the browser that we are going to send the values at runtime
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    # request.config.getoption("browser_name") :to fetch the value of the browser_name key that we pass at run time through the terminal
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
    elif browser_name == "IE":
        print("IE not present")
    # to avoid the return statement
    request.cls.driver = driver
    yield
    driver.close()
