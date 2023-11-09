from utilities.read_Configurations import ReadConfig
from pageObjects.login_page import LoginPage

class BaseClass:
    url = ReadConfig.get_login_url()
    email_id = ReadConfig.get_Emai_id()
    password = ReadConfig.get_password()

    def __init__(self,driver):
        self.driver = driver
        self.log_page = LoginPage(self.driver)
        self.go_to_dashboard_page()

    def go_to_dashboard_page(self):
        self.driver.get(self.url)
        self.log_page.enter_emailId(self.email_id)
        self.log_page.enter_password(self.password)
        self.log_page.clickOn_login_button()
