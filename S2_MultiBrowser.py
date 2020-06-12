from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

# driver = webdriver.Firefox(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\geckodriver-v0.26.0-win64\\geckodriver.exe' )

# driver = webdriver.Ie(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\IEDriverServer_x64_3.150.1\\IEDriverServer.exe' ) ## not working properly

# driver = webdriver.Ie(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\IEDriverServer_Win32_3.150.1\\IEDriverServer.exe' )


driver.get("http://newtours.demoaut.com")

print (driver.title)

print(driver.current_url)

driver.close()
