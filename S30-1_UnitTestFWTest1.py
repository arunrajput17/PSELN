### Python Unit Test Framework

import unittest

class Test(unittest.TestCase):
    def test_firstTest(self):
        print('This is my first unit test case')


# To run this code, we have to make this module as main module

if __name__ == "__main__":
    unittest.main()