#### Implicit wait : is applicable for all the elements on the page. 
# This need to be specified one time at the begining of the code.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.maximize_window()        # to maximize the browser window

driver.get('http://newtours.demoaut.com')

## implicit wait
driver.implicitly_wait(10)      # it waits for maximum 10 seconds

#verify the title of the page
assert 'Welcome: Mercury Tours' in driver.title


# to check username textbox is enabled or not
user_ele= driver.find_element_by_name('userName').send_keys('mercury')

#working on password element
pwd_ele=driver.find_element_by_name('password').send_keys('mercury')

# clicking on login button
driver.find_element_by_name('login').click()


driver.close()



