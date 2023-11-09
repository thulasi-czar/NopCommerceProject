import pytest
from Base.base_page import BaseClass
from pageObjects.add_customer_page import AddCustomer
from utilities.custom_Logger import GenerateLogger
from selenium.webdriver.common.by import By
import allure
import time

@pytest.mark.usefixtures("setupAndteardown")
class Test_002_AddCustomer:
    alert_success_xpath = "//div[@class='alert alert-success alert-dismissable']"
    alert_danger_xpath = "//div[@class='alert alert-danger alert-dismissable']"
    logger = GenerateLogger.gen_logs()
    logger.info("******************** Test Case 002 AddCustomer *************")

    def generate_email(self):
        current_now = time.strftime("%Y-%m-%d_%I-%M-%S")
        email_id = "thulasi"+current_now+"@gmail.com"
        return email_id

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_customer_with_entering_all_fields(self):
        self.logger.info("*************** test case add customer with entering all fields is --started ***************")
        BaseClass(self.driver)
        add_custer_page = AddCustomer(self.driver)
        add_custer_page.go_to_add_customer_category()
        add_custer_page.click_on_customer_list()
        add_custer_page.click_on_AddNew_button()
        add_custer_page.enter_emailId(self.generate_email())
        add_custer_page.enter_password("thulasi")
        add_custer_page.enter_first_name("thulasi")
        add_custer_page.enter_last_name("ashok")
        add_custer_page.select_gender('male')
        add_custer_page.enter_date_of_birth("06/08/1998")
        add_custer_page.enter_company_name("xmt")
        add_custer_page.select_tax_exempt()
        add_custer_page.select_news_letter()
        add_custer_page.click_on_customer_roles_field("Guests")
        add_custer_page.select_vendor("Vendor 1")
        add_custer_page.set_admin_content("This is My Kingdom")
        add_custer_page.click_on_save_button()
        element_exist = self.driver.find_elements(By.XPATH,self.alert_success_xpath)
        if element_exist:
            assert True
            self.logger.info("*************** test case add customer with entering all fields is Passed ***************")
        else:
            self.logger.info("*************** test case add customer with entering all fields is Failed ***************")
            assert False

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_customer_without_entering_anyFields(self):
        self.logger.info("*************** test case add customer without entering any fields is --started ***************")
        BaseClass(self.driver)
        add_custer_page = AddCustomer(self.driver)
        add_custer_page.go_to_add_customer_category()
        add_custer_page.click_on_customer_list()
        add_custer_page.click_on_AddNew_button()
        add_custer_page.click_on_save_button()
        element_exist = self.driver.find_elements(By.XPATH,self.alert_danger_xpath)
        if element_exist:
            assert True
            self.logger.info("*************** test case add customer without entering any fields is Passed ***************")
        else:
            self.logger.info("*************** test case add customer without entering any fields is Failed ***************")
            assert False
