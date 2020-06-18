#### Logging & Log Levels

#  Logging is a very useful tool in a programmer's toolbox. It can help you develop a better understanding
# of the flow of a program and discover scenarios that you might not even have thought of while developing.

# Log Levels (increasing order)
# -DEBUG
# -INFO
# -WARNING
# -ERROR
# -CRITICAL 


import logging

#Config to sent logg in the file
# defining Debug in level will start writing from debug level
logging.basicConfig(filename='D:\\Day Shift\\Zpyth\\Pseln\\TestFiles\\test.log',
format='%(asctime)s: %(levelname)s: %(message)s',
datefmt='%m/%d/%Y %I:%M:%p',
level=logging.DEBUG)

logging.debug('This is debug message')  
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')



