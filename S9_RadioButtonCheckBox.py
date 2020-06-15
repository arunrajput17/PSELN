#### Radio buttons and check boxes

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')


# 1. To verify whether the radio button is already selected or not
status_male = driver.find_element(By.ID,'RESULT_RadioButton-7_0').is_selected()
print('Male radio button status', status_male)

# driver.find_element_by_id('RESULT_RadioButton-7_1').click()
status_female = driver.find_element_by_id('RESULT_RadioButton-7_1').is_selected()
print('Female radio button status ',status_female)

driver.find_element(By.ID,'RESULT_TextField-1').send_keys('John')


# 2. How to click or select 
# driver.find_element_by_id('RESULT_RadioButton-7_0').click()   # this metohd not working in python

## alternate way of click using javacsript
element_male = driver.find_element_by_id('RESULT_RadioButton-7_0')
driver.execute_script('arguments[0].click()',element_male)

#printing status
status_male = driver.find_element(By.ID,'RESULT_RadioButton-7_0').is_selected()
print('Male radio button status after selection ', status_male)

#working with check box
status_sun =driver.find_element_by_id('RESULT_CheckBox-8_0').is_selected()
print('Sun checkbox before status',status_sun)
status_sat =driver.find_element_by_id('RESULT_CheckBox-8_6').is_selected()
print('Sat checkbox before status',status_sat)

# javascript passing multiple arguments
ele_chkSun=driver.find_element_by_id('RESULT_CheckBox-8_0')
ele_chkSat=driver.find_element_by_id('RESULT_CheckBox-8_6')


driver.execute_script('arguments[1].click(); arguments[0].click();', ele_chkSun, ele_chkSat)


status_sun =driver.find_element_by_id('RESULT_CheckBox-8_0').is_selected()
print('Sun checkbox after status',status_sun)
status_sat =driver.find_element_by_id('RESULT_CheckBox-8_6').is_selected()
print('Sat checkbox after status',status_sat)




driver.quit()




















