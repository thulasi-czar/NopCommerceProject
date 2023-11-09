from selenium import webdriver
from selenium.webdriver.common.by import  By
import  time


add_option = webdriver.ChromeOptions()
add_option.add_experimental_option("detach",True)
add_option.add_argument("--start-maximized")

date_icon_xpath = "//input[@id='DateOfBirth']/following-sibling::span"
left_click_xpath = "//div[@id='1b3deb21-84bc-4b76-9094-a3412874abbc']/descendant::a[1]"
right_click_xpath = "//div[@id='1b3deb21-84bc-4b76-9094-a3412874abbc']/descendant::a[3]"
month_year_xpath = "//div[@id='1b3deb21-84bc-4b76-9094-a3412874abbc']/descendant::a[2]"


driver = webdriver.Chrome(options=add_option)
driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/Create")
# driver.find_element(By.XPATH,date_icon_xpath).click()
# msg = driver.find_element(By.XPATH,month_year_xpath).text
# print(msg)

time.sleep(5)
driver.quit()