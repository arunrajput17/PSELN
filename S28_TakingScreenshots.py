#### Take Screen shots

## WebDriver offers API's to take screenshot of a web page
# - save_screenshot('filename')
# - get_screenshot_as_file('filename')

from selenium import webdriver


driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('http://newtours.demoaut.com/')


# Taking screenshot Method 1
driver.save_screenshot('D:\\Day Shift\\Zpyth\\Pseln\\TestFiles\\screenshot1.jpg')   # .jpg .png


# Taking screenshot Method 2
driver.get_screenshot_as_file('D:\\Day Shift\\Zpyth\\Pseln\\TestFiles\\screenshot2.png')



