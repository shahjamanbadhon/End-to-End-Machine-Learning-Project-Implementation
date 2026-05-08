from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

#logging.info("Welcome to my Log.")


try:
    r = 3/0
    print(r)
except Exception as e:
    logging.info(e) #set to log with run demo.py
    raise USvisaException(e, sys)