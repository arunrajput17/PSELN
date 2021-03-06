import unittest
import HtmlTestRunner
from selenium import webdriver
import time

import sys
sys.path.append('D:/Day Shift/Zpyth/Pseln/S42_PythonUnittestPrj_POM/')

from pageObjects.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    baseURL = 'https://admin-demo.nopcommerce.com/'
    username = 'admin@yourstore.com'
    password = 'admin'
    driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\S42_PythonUnittestPrj_POM\\drivers\\chromedriver.exe')
    # driver = webdriver.Chrome(executable_path='..\\drivers\\chromedriver.exe')

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)

        self.assertEqual('Dashboard / nopCommerce administration', self.driver.title, 'Webpage title is not matching')
        
        lp.clickLogout()
        time.sleep(5)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='\\reports'))
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\Day Shift\\Zpyth\\Pseln\\S42_PythonUnittestPrj_POM\\reports'))


####################To Execute use ########################
#   should be in S42_PythonUnittestPrj_POM folder and use below command
#   python testCases/LoginTest.py




