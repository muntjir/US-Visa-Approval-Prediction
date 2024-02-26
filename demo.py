from us_visalogger import logging
from us_visaexception import USvisaException
import sys

try:
    a = 1/"1"
except Exception as e:
    raise USvisaException (e, sys) from e

logging.info("Welcome to our custom vlogger")