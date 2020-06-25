#### PyTest Fixtures
## The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and
# repeatedly execute

import pytest


### @pytest.yield_fixture() : execute specific method before and after every test method

@pytest.yield_fixture()
def setup():
    print('Once before method')
    yield
    print('Once after every method')

def test_Method1(setup):
    print('This is test method 1')

def test_Method2(setup):
    print('This is test method 2')

