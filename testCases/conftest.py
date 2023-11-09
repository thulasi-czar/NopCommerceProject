import pytest
from selenium import webdriver
import time
import allure
import pytest_html
from allure_commons.reporter import AttachmentType

@pytest.fixture(autouse=True)
def setupAndteardown(request):
    browser = request.config.getoption("--browser")
    global driver
    if browser == "chrome":
        add_option = webdriver.ChromeOptions()
        add_option.add_experimental_option("detach",True)
        add_option.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=add_option)
        driver.implicitly_wait(10)
        request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            now = time.strftime("%Y-%m-%d_%H-%M-%S")
            file_path = report.nodeid.replace("::","_")
            file_name = file_path + "_" + now + ".png"
            # get screenshot of failed test case
            driver.get_screenshot_as_file(".\\screenShots\\"+file_name)
            # add screenshot to allure report
            allure.attach(driver.get_screenshot_as_png(),name=file_name,attachment_type=AttachmentType.PNG)
            # add screenshot to html report
            screenshot = driver.get_screenshot_as_base64()
            extras.append(pytest_html.extras.image(screenshot,""))
        report.extras = extras