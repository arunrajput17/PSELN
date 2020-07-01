#### pyTest + HTML Reports (install pytest_html)

from selenium import webdriver
import pytest


class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePageTitle(self,setup):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        assert self.driver.title == 'OrangeHRM123'

    def test_login(self,setup):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()
        assert self.driver.title == 'OrangeHRM'


# Generating PyTest HTML report
# use this default to run test and generate report:
# pytest -v -s --html=report.html Test_S44_PyTestHTMLReport.py

# also we can pass optional command
# pytest -v -s --html=report.html --self-contained-html Test_S44_PyTestHTMLReport.py

# With custom path to save report
# pytest -v -s --html=.\Reports\PyTestHTMLreport.html --self-contained-html  Test_S44_PyTestHTMLReport.py


    


