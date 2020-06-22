#### Assertion : Assertion is nothing but the check point or you can say it as verification for the
# test case to evaluate some item on the execution.
# -- If we do not provide any assertion inside a test case then there is no way to know whether
# a test case is failed or not
# -- Assertion helps in report generation, based on the assertions the test execution report will 
# be generated.
# -- There are few assertion which will accept all the values and few assertion will accept only
# numeric values. 


## assertEqual = assertequal compare the first parameter with the second parameter, if both matches the 
# unittest will continue with the remaining execution but the both the values are differnt then
# unit test fails the testcase.
# 
# 
## assertNotEqual = assertNotEqual method compares the given two parameters, if both parameter are 
# not same then unittest passes the test case but if both parameter are same then unittest fails the 
# test case


import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')
        driver.get('https://www.google.com/')
        titleOfWebPage = driver.title

        # assertEqual
        self.assertEqual('Google',titleOfWebPage, 'Webpage title is not same')

    def testName1(self):
        driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')
        driver.get('https://www.google.com/')
        titleOfWebPage = driver.title

        #assertNotEqual
        self.assertNotEqual('Google1',titleOfWebPage,'Webpage title is same')



if __name__ == "__main__":
    unittest.main()

