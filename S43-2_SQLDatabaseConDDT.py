#### SQL Database Connection & Data Driven Testcase

#### Database operations using Python(cx-Oracle module)
# 1. Connect to database
# 2. how to execute queries (insert, update, delete)
# 3. how to select data from database
# 4. datadriven testing 

from selenium import webdriver
import time
import pyodbc

####### Establish connection to the database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=ACROLAP32\SQLEXPRESS;DATABASE=Sample;UID=sa;PWD=acro')

print(conn)

###### To execute queries (insert, update, delete)

cur = conn.cursor()

query1 = "create table tblUsers(username nvarchar(50) Not Null,password nvarchar(50) Not Null)" #creating table
query2 = "insert into tblUsers values ('abc','abc'),('mercury','mercury'),('mer','merc'),('merc','cury'),('hi','hi')"
query3 = "update tblUsers set password='1234' where username = 'hi'"
query4 = "Delete tblUsers where username ='hi'"
query5 = "Select * from tblUsers"

##### Execution and Selection of data 
cur.execute(query5)


# # fetching data saved in cursor from select query
# for cols in cur:
#     print(cols[0],'    ',cols[1])


##### Data driven testing ( login test)

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('http://newtours.demoaut.com/')
driver.maximize_window()


for cols in cur:
    driver.find_element_by_name('userName').send_keys(cols[0])
    driver.find_element_by_name('password').send_keys(cols[1])
    driver.find_element_by_name('login').click()
    time.sleep(5)

    # validation started
    if driver.title == 'Find a Flight: Mercury Tours:':
        print('Test Passed')
    else:
        print('Test Failed')
    driver.find_element_by_link_text('Home').click()




cur.close()     #Closing cursor
conn.commit()    # commit means insertion is permanent
conn.close() # close connection

print('Complete!!!')

