
from selenium import webdriver
import pytest
from pages.loginpage import loginpage
from pages.homepage import homepage
from Utils import utils as util


class TestLogin():
    @pytest.fixture(scope="session")  #scope = session means browser will open once perform all test cases and than will get close
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("../drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed")



    def test_login(self, test_setup):
        driver.get(util.URL)

        lp = loginpage(driver)
        lp.enter_username(util.USERNAME)
        lp.enter_password(util.PASSWORD)
        lp.click_login()


    def test_logout(self, test_setup):

        hp = homepage(driver)

        hp.click_welcome()
        hp.click_logout()


