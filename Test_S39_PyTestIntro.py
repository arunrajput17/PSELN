#### Pytest intro: Pytest framework makes it easy to write small tests implemented on top of unittest.
# File nam eshould always start with test_

## to run
# pytest 
# pytest -v -s (it will print the details also)
# pytest -v -s Test_Demo.py


import pytest

def testMethod1():
    print('This is test method 1')

def testMethod2():
    print('This is test method 2')

