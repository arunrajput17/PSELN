#### Upload a file

from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()
time.sleep(3)

driver.switch_to_frame(0)       # switching to frame

#uploading file
driver.find_element_by_id('RESULT_FileUpload-10').send_keys('D:\\Day Shift\\Zpyth\\Pseln\\TestFiles\\sample.PNG')


# driver.quit()
