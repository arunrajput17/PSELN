#### Python UnitTest Framework Methods:
# setup : This will execute before every Test Method
# teardown : This will execute after every Test Method
# setUpClass : This will execute once class started
# tearDownClass : This will execute once after the class is completed
# setUpModule :This will execute once before Module is started
# tearDownModule :This will execute once after the Module is completed

import unittest

#######


def setUpModule():  # This will execute once before Module is started
    print('Set up Module')


def tearDownModule():   # This will execute once after the Module is completed
    print('Tear down Module')


class AppTesting(unittest.TestCase):
    @classmethod        # This will execute before every Test Method
    def setUp(self):
        print('This is login test')

    @classmethod
    def tearDown(self):     # This will execute after every Test Method
        print('This is logout test')

    @classmethod
    def setUpClass(cls):    # This will execute once class started
        print('Open Application')

    @classmethod
    def tearDownClass(cls):     # This will execute once after the class is completed
        print('Close Application')

    def test_search(self):
        print('This is search test')

    def test_advancedsearch(self):
        print('This is Advanced search test')

    def test_prepaidRecharge(self):
        print('This is prepaid Recharge test')

    def test_postpaidRecharge(self):
        print('This is post paid Reachage test')




if __name__ == "__main__":
    unittest.main()





