#### Browser windows
# driver.current_window_handle 
# driver.window_handles - it gives handle value of all the woindows

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('http://demo.automationtesting.in/Windows.html')

# Click on click button
driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()

# it will written the parent window handle
print(driver.current_window_handle)

# to get all the widows multiple handles
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=='Frames & windows':
        driver.close()      # close only parent browser






# driver.quit()
