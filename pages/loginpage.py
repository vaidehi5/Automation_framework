class loginpage():

    def __init__(self, driver):
        self.driver = driver

        self.username_txtbox_id = "txtUsername"
        self.password_txtbox_id = "txtPassword"
        self.login_btn_id = "btnLogin"

    def enter_username(self, uname):
        self.driver.find_element_by_id(self.username_txtbox_id).send_keys(uname)

    def enter_password(self, pwd):
        self.driver.find_element_by_id(self.password_txtbox_id).send_keys(pwd)

    def click_login(self):
        self.driver.find_element_by_id(self.login_btn_id).click()




