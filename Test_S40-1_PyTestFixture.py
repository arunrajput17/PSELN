#### PyTest Fixtures
## The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and
# repeatedly execute

import pytest

### @pytest.fixture() : execute specific method before every test method

@pytest.fixture()
def setup():
    print('This is setup method. Once before every method')

def test_Method1(setup):
    print('This is test method 1')

def test_Method2(setup):
    print('This is test method 2')
