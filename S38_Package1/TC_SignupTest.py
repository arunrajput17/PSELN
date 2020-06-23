## TC_SignupTest

import unittest

class SignupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print('This is signup by Email test')
        self.assertTrue(True)

    def test_signupbyFacebook(self):
        print('This is signup by Facebook test')
        self.assertTrue(True)

    def test_signupbyTwitter(self):
        print('This is signup by Twitter test')
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()