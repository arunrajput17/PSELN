#### Links

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('http://newtours.demoaut.com')


## How many links present using common tagname 'a' mostly used
links = driver.find_elements(By.TAG_NAME,'a')
print('Number of links in a page are ',len(links))


## Capture links
for link in links:
    print(link.text)



## Click on the links

# driver.find_element(By.LINK_TEXT,'REGISTER').click()      # using link text

driver.find_element(By.PARTIAL_LINK_TEXT,'REG').click()     # using partial link text


# driver.quit()
