
import pytest

@pytest.yield_fixture()
def setUp():
    print('Opening URL to Login')
    yield
    print('Closing browser after Login')

def test_loginByemail(setUp):
    print('This is login by email test')

def test_loginbyfacebook(setUp):
    print('This is login by facebook user')