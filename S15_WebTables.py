#### HTML / Web Tables

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(5)

# Counting number of rows
rows = len(driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr'))
print('No. of rows: ',rows)

# Counting number of columns

columns = len(driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th'))
print('No. of columns: ',columns)


# Reading data from table

for r in range(2,rows+1):
    for c in range(1,columns+1):
        value =driver.find_element_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr['+str(r)+']/td['+str(c)+']').text
        # print(value)
        print(value,end='       ')        # to display in tabular format
    print()





# driver.quit()
