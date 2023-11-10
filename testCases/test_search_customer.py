import pytest
from Base.base_page import BaseClass
from pageObjects.add_customer_page import AddCustomer
from pageObjects.search_customer_page import SearchCustomer
from utilities.read_Configurations import ReadConfig
from utilities.custom_Logger import GenerateLogger
import allure

@pytest.mark.usefixtures("setupAndteardown")
class Test_003_SearchCustomer:
    email_id = ReadConfig.get_customer_email_id()
    logger = GenerateLogger.gen_logs()
    logger.info("************** Test 003 Search Customer *****************")

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_customer_by_email(self):
        self.logger.info("************** test search customer by email id --started *****************")
        BaseClass(self.driver)
        add_customer_page = AddCustomer(self.driver)
        add_customer_page.go_to_add_customer_category()
        add_customer_page.click_on_customer_list()

        search_page = SearchCustomer(self.driver)
        search_page.enter_email_id(self.email_id)

        #click on search button
        search_page.click_on_search_button()

        status = search_page.search_Customer_by_email(self.email_id)
        if status:
            self.logger.info("************** test search customer by email id Passed *****************")
            assert True
        else:
            self.logger.info("************** test search customer by email id Failed *****************")
            assert False