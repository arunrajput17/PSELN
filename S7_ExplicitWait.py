#### Explicit wait : It is based on the condition not depends on the time. It is based on particular element.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC    #for expected condition used in explicit
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\geckodriver-v0.26.0-win64\\geckodriver.exe' )
driver.implicitly_wait(5)       #implicit wait

driver.maximize_window()        # to maximize the browser window

driver.get('https://www.expedia.com/')

time.sleep(2)

##clicking on Flight icon
# driver.find_element_by_id('tab-flight-tab-hp').click()   # OR we can do it another way mention below
            # OR
driver.find_element(By.ID,'tab-flight-tab-hp').click()



#flying from
driver.find_element(By.ID,'flight-origin-hp-flight').send_keys('SFO')

time.sleep(2)   # python wait

#Going to textbox
driver.find_element(By.ID,'flight-destination-hp-flight').send_keys('NYC')

#Departing date
driver.find_element(By.ID,'flight-departing-hp-flight').clear()     # to clear default values
driver.find_element(By.ID,'flight-departing-hp-flight').send_keys('07/02/2020')

time.sleep(2)

###Returning date

# this method is used to clear default values or auto populated values
driver.find_element(By.ID,'flight-returning-hp-flight').send_keys(Keys.CONTROL + 'a')
driver.find_element(By.ID,'flight-returning-hp-flight').send_keys(Keys.DELETE)     # to clear default values

driver.find_element(By.ID,'flight-returning-hp-flight').send_keys('07/21/2020')

# Click search button
driver.find_element(By.XPATH,'//*[@id="gcw-flights-form-hp-flight"]/div[8]/label/button').click()


####Explicit wait
wait = WebDriverWait(driver,10)     #creating object of wait

element=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="stopFilter_stops-0"]')))

#clicking on Non stop checkbox
element.click()

time.sleep(3)

driver.quit()



