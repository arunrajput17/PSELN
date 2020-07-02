#### How to generate  Allure Reports in Selenium with Python & Pytest

### Agenda
# - Setup Allure on Windows
## https://docs.qameta.io/allure/
## https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.4/


# How to Generate Allure Reports
# How to add Screenshots to Allure REports
# Decorators (for severity)
# How to Share Allure Report

from selenium import webdriver
import allure
import pytest
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.NORMAL)  # decorator for severity at class level
class TestHRM:

    @allure.severity(allure.severity_level.MINOR) # decorator for severity at method level
    def test_Logo(self):
        self.driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        status =self.driver.find_element_by_xpath('//*[@id="divLogo"]/img').is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.close()


    @allure.severity(allure.severity_level.MINOR) # decorator for severity at method level
    def test_listemployees(self):
        pytest.skip('Skipping test.. later I will implement..')


    @allure.severity(allure.severity_level.BLOCKER) # decorator for severity at method level
    # @allure.severity(allure.severity_level.CRITICAL) # decorator for severity at method level
    def test_Login(self):
        self.driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()
        act_title = self.driver.title 

        if act_title == 'OrangeHRM123':
            self.driver.close()
            assert True
        else:
            # Taking screenshot of fail test
            allure.attach(self.driver.get_screenshot_as_png(),name='testLoginScreen',
            attachment_type=AttachmentType.PNG)

            self.driver.close()
            assert False

###### To Execute and generate allure report:
## pytest -v -s --alluredir=".\Reports"  Test_S45_PyTestAllureReport.py 
## OR Path like pytest -v -s --alluredir="D:\R"  Test_S45_PyTestAllureReport.py 

### To view allure report
# In CMD we need to write command 
# allure serve D:\R

### Share allure report with others
#-- We cannot Export allure reports to a single HTML file
#-- Because allure report is not a simple webpage. We cannot save it and send as file to your team.
#-- It's a local Jetty server instance, serves generated report and then you can opens it in the browser.

###########################################
## create login in netlify.com 
## in deployment area we need to  drag and drop folder which is create when we execute in cmd it generated
# temp folder that we need to copy
# then it will generate the link and by using it we can access report in browser 

 
