#### Navigation commands : navigate using browser arrows to move back forwward in browser history page

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('http://newtours.demoaut.com')

print(driver.title) 

driver.get('http://www.pavantestingtools.com/')

time.sleep(5)
print(driver.title)

driver.back()   # navigating using browser arrow back button

time.sleep(5)
print(driver.title)

driver.forward()    # navigating using browser forward button

time.sleep(5)
print(driver.title)

driver.close()
