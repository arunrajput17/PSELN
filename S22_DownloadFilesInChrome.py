#### Download a file in chrome browser

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

# Runtime downloading the file at expected location need to import 'Options'
chromeOptions = Options()
chromeOptions.add_experimental_option('prefs',{'download.default_directory':'D:\\Day Shift\\Zpyth\\Pseln\\TestFiles'})

# add chorome options 
driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe',chrome_options=chromeOptions)

driver.get('http://demo.automationtesting.in/FileDownload.html')

driver.maximize_window()
time.sleep(3)

# Download a text file
driver.find_element_by_id('textbox').send_keys('Testing download text file')
driver.find_element_by_id('createTxt').click()    # click on generate file button
driver.find_element_by_id('link-to-download').click()   # Download file on default location



# Download pdf file
driver.find_element_by_id('pdfbox').send_keys('Testing download pdf file')
driver.find_element_by_id('createPdf').click()  # click on generate file button
driver.find_element_by_id('pdf-link-to-download').click()   # Download file on default location




# driver.quit()
