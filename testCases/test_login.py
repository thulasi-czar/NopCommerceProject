import pytest
from utilities.read_Configurations import ReadConfig
from pageObjects.login_page import LoginPage
from utilities.custom_Logger import GenerateLogger
import allure

@pytest.mark.usefixtures("setupAndteardown")
class Test_001_Login:
    url = ReadConfig.get_login_url()
    logger = GenerateLogger.gen_logs()
    email_Id = ReadConfig.get_Emai_id()
    password = ReadConfig.get_password()
    base_page_title = "Your store. Login"
    expected_page_title = "Dashboard / nopCommerce administration"
    logger.info("**************** Test Case 001 Login ******************")

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_valid_credentials(self):
        self.logger.info("************* login with valid credentials ---started **************")
        self.driver.get(self.url)
        login_page = LoginPage(self.driver)
        login_page.enter_emailId(self.email_Id)
        login_page.enter_password(self.password)
        login_page.clickOn_login_button()
        actual_page_title = self.driver.title

        if actual_page_title.__eq__(self.expected_page_title):
            self.logger.info("********** login with valid credentials test case is passed ************")
            assert True
        else:
            self.logger.info("********* login with valid credentials test case is failed **************")
            assert False

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_invalid_credentials(self):
        self.logger.info("**************** login with invalid credentials -----started ******************")
        self.driver.get(self.url)
        login_page = LoginPage(self.driver)
        login_page.enter_emailId("thulasi@gmail.com")
        login_page.enter_password("ashok")
        login_page.clickOn_login_button()
        actual_page_title = self.driver.title
        if actual_page_title.__eq__(self.base_page_title):
            assert True
            self.logger.info("*************** login with invalid credentials test case is passed ****************")
        else:
            self.logger.info("*************** login with invalid credentials test case is failed ****************")
            assert False

