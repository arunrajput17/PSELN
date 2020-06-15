#### Handle Frames / iFrames
# switch_to.frame(name)
#switch_to.frame(id)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html')

# switching to First frame click on org.openqa.selenium
driver.switch_to_frame('packageListFrame')          # switching to first frame
driver.find_element(By.LINK_TEXT,'org.openqa.selenium').click()
time.sleep(3)

#### Go back to main frame before switching to another frame this is mandatory we can not 
# directly switch  between frames

driver.switch_to.default_content()

# switch to second frame
driver.switch_to.frame('packageFrame')      # switch to second frame
driver.find_element(By.LINK_TEXT,'WebDriver').click()
time.sleep(3)


# Switch to default frame
driver.switch_to.default_content()
time.sleep(3)

# Switch to third frame
driver.switch_to.frame('classFrame')                  # switch to third frame
driver.find_element(By.XPATH,'/html/body/div[1]/ul/li[5]').click()



# driver.quit()
