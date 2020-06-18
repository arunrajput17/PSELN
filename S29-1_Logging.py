#### Logging & Log Levels (Using Logger object)



import logging

#Config to sent logg in the file
# defining Debug in level will start writing from debug level
logging.basicConfig(filename='D:\\Day Shift\\Zpyth\\Pseln\\TestFiles\\test.log',
format='%(asctime)s: %(levelname)s: %(message)s',
datefmt='%m/%d/%Y %I:%M:%p')

##Creating logger object
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug('This is debug message')  
logger.info('This is info message')
logger.warning('This is warning message')
logger.error('This is error message')
logger.critical('This is critical message')



