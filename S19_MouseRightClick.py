#### Mouse actions : Mouse Right Click

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')

driver.maximize_window()
time.sleep(3)

button = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')

# Mouse right click
actions = ActionChains(driver)

actions.context_click(button).perform()     # right click action


# driver.quit()
