import XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('http://newtours.demoaut.com/')
driver.maximize_window()

path = 'D:\\Day Shift\\Zpyth\\Pseln\\TestFiles\\data26.xlsx'

rows = XLUtils.getRowCount(path, 'Sheet1')
# print(rows)


for r in range(2,rows+1):
    username = XLUtils.readData(path, 'Sheet1', r, 1)
    password = XLUtils.readData(path, 'Sheet1', r, 2)
    # print(username,'===',password)

    driver.find_element_by_name('userName').send_keys(username)
    driver.find_element_by_name('password').send_keys(username)

    driver.find_element_by_name('login').click()
    if driver.title == 'Find a Flight: Mercury Tours:':
        print('Test is passed')
        XLUtils.writeData(path, 'Sheet1', r, 3, 'Test passed')
    else:
        print('Test Failed')
        XLUtils.writeData(path, 'Sheet1', r, 3, 'Test failed')

    driver.find_element_by_link_text('Home').click()







