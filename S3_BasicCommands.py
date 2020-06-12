from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome
driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.maximize_window()

driver.get('http://demo.automationtesting.in/Windows.html')

print(driver.title)     # returns the title of the page

print(driver.current_url)   # returns URL of the page

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

time.sleep(5)

# driver.close()    # currently focused browser

driver.quit()   # closes all the browser
