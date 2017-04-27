# -*- coding: utf-8 -*-
"""Logging configuration."""

import sys
import os

import logging

from logging import handlers

logging.getLogger('UI').addHandler(logging.NullHandler())

LOGGER_NAME = 'storj-python-gui-log'
LOG_FILENAME = 'test.log'
PATH = os.path.join(os.getcwd(), LOG_FILENAME)

logger = logging.getLogger(LOGGER_NAME)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# Logs written to file
# Rotating file logger. Max size 3 MB per 5 log files
fileHandler = handlers.RotatingFileHandler(
    PATH,
    maxBytes=(1048576 * 3),
    backupCount=5)

fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.WARNING)
logger.addHandler(fileHandler)

# Logs to stdout
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
consoleHandler.setLevel(logging.DEBUG)
logger.addHandler(consoleHandler)
