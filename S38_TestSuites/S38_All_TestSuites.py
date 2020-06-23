## All_TestSuites

import unittest

## Importing all the classes from packages
from S38_Package1.TC_LoginTest import LoginTest
from S38_Package1.TC_SignupTest import SignupTest
from S38_Package2.TC_PaymentReturnsTest import PaymentReturnsTest
from S38_Package2.TC_PaymentTest import PaymentTest

# Get all tests from LoginTest, SignupTest, PaymentTest and PaymentReturnsTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating Test Suites
sanityTestSuite = unittest.TestSuite([tc1,tc2])   # Sanity Test suite
funtionalTestSuite = unittest.TestSuite([tc3,tc4])  # Functional test suite
masterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4]) # Master test suite

# Execution
# unittest.TextTestRunner().run(sanityTestSuite)  # Execute Sanity test suite
# unittest.TextTestRunner().run(funtionalTestSuite)   # Execute Funtional test suite

# Another way of execution with verbosity will give detail info
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)  #Execute Master test suite
