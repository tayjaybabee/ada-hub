"""

A module containing some constants for AdaHub's runtime.

"""

from platform import system
from os import getpid
from pathlib import Path

PROG = 'AdaHub'
PID = getpid()

HOME_DIR = f'{ Path.home() }/'

DEFAULT_DATA_ROOT = str(f'{HOME_DIR}Inspyre-Softworks/{PROG}/')
DEFAULT_CONF_ROOT = str(f'{DEFAULT_DATA_ROOT}conf/')

default_conf_file_name = 'settings'
default_conf_file_ext = 'ini'
DEFAULT_CONF_FILE_PATH = str(f'{DEFAULT_CONF_ROOT}{default_conf_file_name}.{default_conf_file_ext}')

LOG_LEVELS = ['debug', 'info', 'warning', 'error']


