#### Input box:

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

# 1. How to find how many input boxes present in web page
inputboxes = driver.find_elements(By.CLASS_NAME,'text_field')
print('Number os textboxes are ',len(inputboxes))


# 2. How to get the status of text box
status = driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print('Displayed or not ', status)

status = driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print('Enabled or not', status)



# 3. How to provide value into text box
driver.find_element(By.ID,'RESULT_TextField-1').send_keys('John')
driver.find_element(By.ID,'RESULT_TextField-2').send_keys('Ceana')

#other meythod
driver.find_element_by_id('RESULT_TextField-3').send_keys('111111111')


driver.quit()


