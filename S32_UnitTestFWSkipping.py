#### Python UnitTest Framework : Skipping tests
# - Skip Test
# - Skip Test with reason
# - Skip Test with Based on condition

import unittest

#######

class AppTesting(unittest.TestCase):

    @unittest.SkipTest      #   This decorator will skip this Test Method execution
    def test_search(self):
        print('This is search test')

    @unittest.skip('I am skipping this method bcoz it is not yet ready ')
    def test_adncedsearch(self):
        print('This is advanced search method')

    @unittest.skipIf(1==1,' 1 is equals to 1')
    def test_prepaidrecharge(self):
        print('This is prepaid recharge test')

    def test_postpaidrecharge(self):
        print('This is postpaid recharge test')
    
    def test_loginbygmail(self):
        print('This is login by email test')

    def test_loginbytwitter(self):
        print('This is login by twitter')


if __name__ == "__main__":
    unittest.main()



