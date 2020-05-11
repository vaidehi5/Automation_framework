import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="type in browser name e.g chrome or firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome("D:/python_projects/Automation_framework/drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Chrome("../driver/chromedriver.exe")


    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("test completed")