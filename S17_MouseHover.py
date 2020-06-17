#### Mouse actions : Mouse Hover

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('https://opensource-demo.orangehrmlive.com/')

driver.maximize_window()
time.sleep(3)


driver.find_element_by_id('txtUsername').send_keys('Admin')     # User name
driver.find_element_by_id('txtPassword').send_keys('admin123')  #password
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()     # Login button

print(driver.title)

admin=driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
usermgmt = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
users = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

## Mouse hover action
action = ActionChains(driver)   # creted object of ActioChains 

action.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()



# driver.quit()
