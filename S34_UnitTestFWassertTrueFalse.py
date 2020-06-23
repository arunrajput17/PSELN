#### assertTrue:
# - when we have only two parameter we can use assertEqual method to check whether both are same or not,
#  but if we have more than two parameters, comparing values with assertEqual method become more difficult.
# - assertTrue method checks whether given parameter is true or not, if value is true then test is passed
# otherwise test is failed.
# 
#### assertFalse:
# assertFalse method compares whether given value or expression results in false or not.
# - if the result or value is False then unittest passes the testcase but if the result or value is True
# then unittest fails the test case.

import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')
        driver.get('https://www.google.com/')
        titleOfWebPage = driver.title
        
        #assertTrue
        self.assertTrue(titleOfWebPage == 'Google')

    def testName1(self):
        driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')
        driver.get('https://www.google.com/')
        titleOfWebPage = driver.title
        
        #assertFalse
        self.assertFalse(titleOfWebPage == 'Google1')


if __name__ == '__main__' :
    unittest.main()

