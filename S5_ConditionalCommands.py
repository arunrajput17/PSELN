#### Conditional commands : 'is_displayed()','is_enabled','is_selected'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.maximize_window()        # to maximize the browser window

driver.get('http://newtours.demoaut.com')

# to check username textbox is enabled or not
user_ele= driver.find_element_by_name('userName')

print(user_ele.is_displayed())       # returns Trure or False based on element status

# To check element is enabled or not
print(user_ele.is_enabled())         # returns True or False based on status of element.


#working on password element
pwd_ele=driver.find_element_by_name('password')
print(pwd_ele.is_displayed())       # returns Trure or False based on element status
print(pwd_ele.is_enabled())         # returns Trure or False based on element status


# Enetering data in textbox
user_ele.send_keys('mercury')
pwd_ele.send_keys('mercury')

# clicking on login button
driver.find_element_by_name('login').click()

# after login working on Radio button
## writing  CSS selector by own: tagname [unique attribute]

roundtrip_radio = driver.find_element_by_css_selector('input[value=roundtrip]')

print('Status of roundtrip radio button is ',roundtrip_radio.is_selected())       # returns Trure or False based on element status

oneway_radio = driver.find_element_by_css_selector('input[value=oneway')
print('Status of oneway radio button is ',oneway_radio.is_selected())           # returns Trure or False based on element status


driver.close()



