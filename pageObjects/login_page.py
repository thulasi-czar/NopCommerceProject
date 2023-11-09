from selenium.webdriver.common.by import By

class LoginPage:
    email_fieldbox_xpath = "//input[@id='Email']"
    password_fieldbox_xpath = "//input[@id='Password']"
    login_button_xpath = "//button[normalize-space(text())='Log in']"

    def __init__(self,driver):
        self.driver = driver

    def enter_emailId(self,email):
        email_filedBox = self.driver.find_element(By.XPATH,self.email_fieldbox_xpath)
        email_filedBox.clear()
        email_filedBox.send_keys(email)

    def enter_password(self,password):
        password_fieldBox = self.driver.find_element(By.XPATH,self.password_fieldbox_xpath)
        password_fieldBox.clear()
        password_fieldBox.send_keys(password)

    def clickOn_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

