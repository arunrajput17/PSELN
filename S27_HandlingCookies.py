##### Handling Cookies

### Operations on Cookies

# 1. Capture all cookies from browser
# 2. Count number of cookies
# 3. Read Cookie pair
# 4. Adding new cookies
# 5. Deleting specific cookie by using name of cookie
# 6. Deleting all the cookies


from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:\\Day Shift\\Zpyth\\Pseln\\External Libraries\\chromedriver_win32\\chromedriver.exe')

driver.get('https://www.amazon.in/')


# 1. Capture all cookies from browser
cookies = driver.get_cookies()

# 2. Count number of cookies
print('Length of cookies :', len(cookies))

# 3. Read Cookie pair
print(cookies)

# 4. Adding new cookies
cookie ={'name':'Mycookie', 'value':'1234567890'}

driver.add_cookie(cookie)

cookies = driver.get_cookies()
print('After adding new cookie :', len(cookies))    # length after adding cookie
print(cookies)      # print all the cookie pair


# 5. Deleting specific cookie by using name of cookie

driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print('After deleting new cookie :', len(cookies))    # length after deleting cookie
print(cookies)   # print all the cookie pair after deleting

# 6. Deleting all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print('After deleting all cookies :', len(cookies))
print(cookies)




