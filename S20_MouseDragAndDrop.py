#### Mouse actions : Mouse DRag and Drop

from selenium import webdriver
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

driver.maximize_window()
time.sleep(3)

# identifying source and target elements
source_element =driver.find_element_by_xpath('//*[@id="box6"]')
target_element = driver.find_element_by_xpath('//*[@id="box106"]')


# Drag and drop
actions = ActionChains(driver)


actions.drag_and_drop(source_element,target_element).perform()




# driver.quit()
