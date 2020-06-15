#### Dropdown list

from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')


#### 1. select one option

# drp=Select(driver.find_element_by_id('RESULT_RadioButton-9'))      
##  OR

element = driver.find_element_by_id('RESULT_RadioButton-9')
drp= Select(element)

# Select value by visible text
drp.select_by_visible_text('Morning')

# Select by index number
drp.select_by_index(2)

# Select by value
drp.select_by_value('Radio-2')


#### 2. Count how many options present

print(len(drp.options))

#### 3. Capture options from drop down
all_options = drp.options

for option in all_options:
    print(option.text)




# driver.quit()
