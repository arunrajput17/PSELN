#### Unittest + HTML Reports + Page Object Model

## Selenium Python Test Case Unit Test, HTML Reports

from selenium import webdriver
import unittest
import HtmlTestRunner


class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        self.assertEqual('OrangeHRM1',self.driver.title, 'Webpage title is not matching')

    def test_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()
        self.assertEqual('OrangeHRM',self.driver.title, 'Webpage title is not matching')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('Test completed....')


if __name__ == '__main__':
        # this is added to generate HTML report
        # Note : Html reports will generate if we execute programm using (python Test_S42_HTMLReport.py)
        #  instead of pytest command
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\Day Shift\\Zpyth\\Pseln\\Reports'))     


    


