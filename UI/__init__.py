# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import os


import click
import logging
import logging.config as config


from logging import handlers


APP_NAME = 'storj-gui'
"""(str): the application name."""


def setup_logging():
    """Reads the Storj GUI logging configuration from logging.conf.
    If the file does not exist it will load a default configuration.

    Mac OS X (POSIX):
        ~/.storj-gui
    Unix (POSIX):
        ~/.storj-gui
    Win XP (not roaming):
        ``C:\Documents and Settings\<user>\Application Data\storj-gui``
    Win 7 (not roaming):
        ``C:\\Users\<user>\AppData\Local\storj-gui``
    """

    logging_conf = os.path.join(
        click.get_app_dir(APP_NAME, force_posix=True),
        'logging.conf')

    if not os.path.exists(logging_conf) or not os.path.isfile(logging_conf):
        load_default_logging()
        logging.getLogger(__name__).warning('%s logging configuration file does not exist', logging_conf)
        return

    try:
        config.fileConfig(logging_conf, disable_existing_loggers=False)
        logging.getLogger(__name__).info('%s configuration file was loaded.', logging_conf)

    except RuntimeError:
        load_default_logging()
        logging.getLogger(__name__).warning('failed to load configuration from %s', logging_conf)
        return

    logging.getLogger(__name__).info('using logging configuration from %s', logging_conf)


def load_default_logging():
    """Load default logging configuration:

    - >=INFO messages will be written to storj-gui.log
    - >=DEBUG messages will be written to stdout
    - >=ERROR message will be written to stderr
    """
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # file
    # maximum of 5 log files of 3MB
    handler_file = handlers.RotatingFileHandler(
        os.path.join(os.getcwd(), '%s.log' % APP_NAME),
        maxBytes=(1048576 * 3), backupCount=5)
    handler_file.setFormatter(formatter)
    handler_file.setLevel(logging.INFO)

    # stdout
    handler_stdout = logging.StreamHandler(sys.stdout)
    handler_stdout.setFormatter(formatter)
    # stdout should only get WARNING, INFO and DEBUG
    handler_stdout.setLevel(logging.DEBUG)

    # stderr
    handler_stderr = logging.StreamHandler(sys.stderr)
    handler_stderr.setFormatter(formatter)
    handler_stderr.setLevel(logging.ERROR)

    logger = logging.getLogger(__name__)
    logger.addHandler(handler_file)
    logger.addHandler(handler_stdout)

    logging.getLogger(__name__).info('using default logging configuration')

setup_logging()
