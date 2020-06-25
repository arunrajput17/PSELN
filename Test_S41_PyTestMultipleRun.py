#### Multiple ways to Run Test Cases

## py.test test_mod.py      # run tests in module
# pytest -v -s Test_S41-1_Login.py


## py.test somepath         # run all tests below somepath
# pytest -v -s D:\Day Shift\Zpyth\Pseln\S41_Pack\

## py.test test_modul.py::test_method   # only run test_method in test_module
# pytest -v -s Test_S41-1_Login.py::test_loginByemail

# -s to print statements
# -v verbose

# cd S41_Pack
#
