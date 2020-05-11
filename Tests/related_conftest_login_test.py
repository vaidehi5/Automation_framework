
from selenium import webdriver
import moment
import pytest
from pages.loginpage import loginpage
from pages.homepage import homepage
from Utils import utils as util
import allure

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(util.URL)

        lp = loginpage(driver)
        lp.enter_username(util.USERNAME)
        lp.enter_password(util.PASSWORD)
        lp.click_login()


    def test_logout(self):

        try:
            driver = self.driver
            hp = homepage(driver)

            hp.click_welcome()
            hp.click_logout()
            x = driver.title
            assert x == "abc"

        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currenttime = moment.now().strftime("%d-%m-%y_%H-%M-%S")
            testname = util.whoami()
            screenshotname = testname+"_" + currenttime
            allure.attach(self.driver.get_screenshot_as_png(), name =screenshotname, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("D:/python_projects/Automation_framework/screenshots"+ screenshotname + ".png")
            raise

        except:
            print("this was an exception")
            raise

        else:
            print("no exception occured")

        finally:
            print("I am inside finally block")
