#### Oracle Database Connection

# SQL --> is a language by which we can communicate with the database.
# 
#### SQL commands
# DDL (Data Definition Language) --> create, alter, drop
# DML (Data Manipulation Language) --> Insert, update, delete
# DRL (Data Retrival Language) --> Select
# DCL (Data Control Language) --> Grant, Revoke
# TCL (Transaction Control Language) --> Commit, savepoint etc..
# 
# 
#### Connection Details:
# Server IP / name
# port no.
# username/password
# servicename / id / databasename 
# 

#### Pre-requisites
# 1. Oracle database 
#         http://www.oracle.com/webfolder/technetwork/tutprials/obe/db/12c/rl/Windows_DB_Install_OBE/Intalling_Oracle_Db12c_Windows.html 
# 2. Oracle instant client
#         https://www.oracle.com/technetwork/topics/winsoft-085727.html
# 3. cx_Oracle through command prompt
#         pip install cx-Oracle
# 4. cx-Oracle in Python 
#         Select project --> file --> settings--> project Interpreter --> + --> cx_Oracle --> select--> install package



#### To install Oracle in python
# pip install cx-Oracle
#
#### Database operations using Python(cx-Oracle module)
# 1. Connect to database
# 2. how to execute queries (insert, update, delete)
# 3. how to select data from database
# 4. datadriven testing 

from selenium import webdriver
import time
import cx_Oracle
import os
os.environ['PATH']='D:\\app\\OracleHomeUser1\\instantclient_10_3'    # Location of instant client


####### Establish connection to the database
#  cx_Oracle.Connect('username','password','oracle ip address/servername')
con=cx_Oracle.Connect('hr','hr','localhost/pdborcl')

print(con)

####### To execute queries (insert, update, delete)

cur = con.cursor()

cur.execute('select * from student')

# cur.execute("insert into student values(102, 'JOHN')"")  # Insert data

query1 = "insert into student values(102, 'JOHN')"
query2 = "update student set sname='XYZ' where sid=102"
query3 = "Delete student where sid=102"

cur.execute(query2)

##### Selection of data 
query4 = "Select * from employees"
cur.execute(query4)

# fetching data saved in cursor from select query
for cols in cur:
    print(cols[0],'    ',cols[1],'    ',cols[2])


##### Data driven testing ( login test)
# select * from users
#   username    password
#   abc         abc
#   mercury     mercury
#   mer         merc
#   merc        curv

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('http://newtours.demoaut.com/')
driver.maximize_window()

query5 = "Select * from users"
cur.execute(query5)

for cols in cur:
    driver.find_element_by_name('username').send_keys(cols[0])
    driver.find_element_by_name('password').send_keys(cols[1])
    driver.find_element_by_name('login').click()
    time.sleep(5)

    # validation started
    if driver.title == 'Find a Flight: Mercury Tours:':
        print('Test passed')
    else:
        print('Test Failed')
    driver.find_element_by_link_text('Home').click()




cur.close()     #Closing cursor
con.commit()    # commit means insertion is permanent
con.close() # close connection

print('Complete!!!')

