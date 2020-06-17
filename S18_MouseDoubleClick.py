#### Mouse actions : Mouse Double Click

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()
time.sleep(3)


element = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')

# Double click
actions = ActionChains(driver)

actions.double_click(element).perform()


# driver.quit()
