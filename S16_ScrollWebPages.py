#### Scroll web pages

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')

driver.maximize_window()
time.sleep(3)

## Scroll down the page by pixel
driver.execute_script('window.scrollBy(0,1000)','')
time.sleep(3)


## Scroll down the page till element found
flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
driver.execute_script('arguments[0].scrollIntoView();',flag)
time.sleep(3)

## Scroll to end of the page
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')





# driver.quit()
