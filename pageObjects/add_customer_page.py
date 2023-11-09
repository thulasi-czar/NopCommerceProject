from selenium.webdriver.common.by import  By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.select import Select

class AddCustomer:
    customer_category_xpath = "//p[normalize-space(text())='Customers']"
    # customer_list_xpath = "//a[@href='/Admin/Customer/List']/child::p"
    customer_list_xpath = "//a[@href='/Admin/Customer/List']"
    add_new_btn_xpath = "//div[@class='float-right']/a"
    email_field_box_xpath = "//input[@id='Email']"
    password_field_box_xpath = "//input[@id='Password']"
    first_name_field_box_xpath = "//input[@id='FirstName']"
    last_name_field_box_xpath = "//input[@id='LastName']"
    rd_male_xpath = "//input[@id='Gender_Male']"
    rd_female_xpath = "//input[@id='Gender_Female']"
    dob_xpath = "//input[@id='DateOfBirth']"
    company_name_xpath = "//input[@id='Company']"
    tax_exempt_xpath = "//input[@id='IsTaxExempt']"
    news_letter_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']/parent::div"
    news_letter_option_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/child::li[2]"
    cutomer_roles_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']/parent::div"
    list_item_registered_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'Registered')]"
    list_item_administrator_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'Administrators')]"
    list_item_vendors_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'Vendors')]"
    list_item_guests_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'Guests')]"
    vendor_drp_dwn_xpath = "//select[@id='VendorId']"
    drp_dwn_id = "VendorId"
    admin_cntnt_xpath = "//textarea[@id='AdminComment']"
    save_btn_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def go_to_add_customer_category(self):
        self.driver.find_element(By.XPATH,self.customer_category_xpath).click()

    def click_on_customer_list(self):
        self.driver.find_element(By.XPATH,self.customer_list_xpath).click()

    def click_on_AddNew_button(self):
        self.driver.find_element(By.XPATH,self.add_new_btn_xpath).click()

    def enter_emailId(self,email_id):
        email_field_box = self.driver.find_element(By.XPATH,self.email_field_box_xpath)
        email_field_box.clear()
        email_field_box.send_keys(email_id)

    def enter_password(self,password):
        password_field_box = self.driver.find_element(By.XPATH,self.password_field_box_xpath)
        password_field_box.clear()
        password_field_box.send_keys(password)

    def enter_first_name(self,name):
        first_name_field_box = self.driver.find_element(By.XPATH,self.first_name_field_box_xpath)
        first_name_field_box.clear()
        first_name_field_box.send_keys(name)

    def enter_last_name(self,name):
        last_name_field_box = self.driver.find_element(By.XPATH,self.last_name_field_box_xpath)
        last_name_field_box.clear()
        last_name_field_box.send_keys(name)

    def select_gender(self,gender):
        if gender.lower() == "male":
            self.driver.find_element(By.XPATH,self.rd_male_xpath).click()
        elif gender.lower() == "female":
            self.driver.find_element(By.XPATH,self.rd_female_xpath).click()

    def enter_date_of_birth(self,dob):
        self.driver.find_element(By.XPATH,self.dob_xpath).send_keys(dob)

    def enter_company_name(self,name):
        self.driver.find_element(By.XPATH,self.company_name_xpath).send_keys(name)

    def select_tax_exempt(self):
        self.driver.find_element(By.XPATH,self.tax_exempt_xpath).click()

    def select_news_letter(self):
        self.driver.find_element(By.XPATH,self.news_letter_xpath).click()
        self.driver.find_element(By.XPATH,self.news_letter_option_xpath).click()

    def click_on_customer_roles_field(self,role):
        self.driver.find_element(By.XPATH,self.cutomer_roles_xpath)
        if role == "Registered":
            pass
        else:
            if role == "Administrators":
                self.role_list = self.driver.find_element(By.XPATH,self.list_item_administrator_xpath)
            elif role == "Guests":
                self.driver.execute_script("arguments[0].click();",self.driver.find_element(By.XPATH,self.list_item_registered_xpath))
                self.role_list = self.driver.find_element(By.XPATH,self.list_item_guests_xpath)
            elif role == "Vendors":
                self.role_list = self.driver.find_element(By.XPATH,self.list_item_vendors_xpath)
            self.driver.execute_script("arguments[0].click();",self.role_list)

    def select_vendor(self,title):
        drp_dwn = Select(self.driver.find_element(By.XPATH,self.vendor_drp_dwn_xpath))
        drp_dwn.select_by_visible_text(title)

    def set_admin_content(self,text):
        self.driver.find_element(By.XPATH,self.admin_cntnt_xpath).send_keys(text)

    def click_on_save_button(self):
        self.driver.find_element(By.XPATH,self.save_btn_xpath).click()

