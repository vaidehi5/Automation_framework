class homepage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link = "welcome"
        self.logout_link = "Logout"

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link).click()


