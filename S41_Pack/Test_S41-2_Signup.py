
import pytest

@pytest.yield_fixture()
def setUp():
    print('Opening URL to signup')
    yield
    print('Closing browser after signup')

def test_signupByemail(setUp):
    print('This is signup by email test')

def test_signupbyfacebook(setUp):
    print('This is signup by facebook user')