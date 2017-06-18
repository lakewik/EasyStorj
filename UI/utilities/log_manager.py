import logging
import os
import sys
# Submodule. Necessary explicit import
from logging import handlers


LOGGER_NAME = 'storj-python-gui-log'
LOG_FILENAME = 'test.log'
PATH = os.path.join(os.getcwd(), LOG_FILENAME)

logger = logging.getLogger(LOGGER_NAME)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# Logs written to file
# Rotating file logger. Max size 3 MB per 5 log files
fileHandler = handlers.RotatingFileHandler(PATH,
                                           maxBytes=(1048576 * 3),
                                           backupCount=5)
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.WARNING)
# fileHandler.setLevel(logging.DEBUG)  # TODO: change to WARNING
logger.addHandler(fileHandler)

# Logs to stdout
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
consoleHandler.setLevel(logging.DEBUG)
logger.addHandler(consoleHandler)
