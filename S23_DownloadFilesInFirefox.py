#### Download a file in Firefox browser

from selenium import webdriver
import time

# Runtime downloading the file from firefox
fp = webdriver.FirefoxProfile()

fp.set_preference('browser.helperApps.neverAsk.saveToDisk','text/plain,application/pdf')    # Mine type (text/plain)
fp.set_preference('browser.download.manager.showWhenStarting',False)
fp.set_preference('browser.download.dir','D:\\Day Shift\\Zpyth\\Pseln\\TestFiles')
fp.set_preference('browser.download.folderList',2)
fp.set_preference('pdfjs.disabled',True)



driver = webdriver.Firefox(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\geckodriver-v0.26.0-win64\\geckodriver.exe',firefox_profile=fp)

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
