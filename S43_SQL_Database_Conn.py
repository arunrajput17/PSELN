#### SQL Database connection


import pyodbc

##### Windows Authentication
# conn = pyodbc.connect("Driver={SQL Server};"
#                      "Server=ACROLAP32\SQLEXPRESS;"
#                      "Database=Sample;"
#                      "username=sa;"
#                      "password=acro;"
#                      "Trusted_Connection=yes;")

####            OR
# conn = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = 'ACROLAP32\SQLEXPRESS', database = 'Sample')

###### SQL Server Authentication
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=ACROLAP32\SQLEXPRESS;DATABASE=Sample;UID=sa;PWD=acro')

cursor = conn.cursor()
cursor.execute('select * from dbo.tblEmployee')

for row in cursor:
    print(row)

