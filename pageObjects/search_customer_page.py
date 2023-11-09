import pytest
from selenium.webdriver.common.by import By

class SearchCustomer:
    email_field_box_xpath = "//input[@id='SearchEmail']"
    search_btn_xpath = "//button[@id='search-customers']"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']/tbody/tr"
    not_found_xpath = "//td[contains(text(),'No data available in table')]"
    data_found_xpath = "//table[@id='customers-grid']/tbody/tr/td[2]"

    def __init__(self,driver):
        self.driver = driver

    def enter_email_id(self,email_id):
        email_field_box = self.driver.find_element(By.XPATH,self.email_field_box_xpath)
        email_field_box.clear()
        email_field_box.send_keys(email_id)

    def get_no_of_rows(self):
        table = self.driver.find_element(By.XPATH, self.table_xpath)
        rows = table.find_elements(By.XPATH,self.table_rows_xpath)
        length = len(rows)
        return length

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.search_btn_xpath).click()

    def search_Customer_by_email(self,email_id):
        data_not_found = self.driver.find_elements(By.XPATH,self.not_found_xpath)
        if data_not_found:
            return False
        else:
            found_id = self.driver.find_element(By.XPATH,self.data_found_xpath).text
            if found_id == email_id:
                return True
            else:
                return False


































        # for i in range(1,self.get_no_of_rows()):
        #     table = self.driver.find_element(By.XPATH,self.table_xpath)
        #     result_id = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(i)+"]/td[2]").text
        #     if email_id == result_id:
        #         print(result_id)
        #         return True
        # return False
