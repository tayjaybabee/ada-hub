"""

A module containing some constants for AdaHub's runtime.

"""

from ada_hub.lib.helpers import home_dir_find
from platform import system
from os import getpid

PROG = 'AdaHub'
PID = getpid()

HOME_DIR = home_dir_find()

DEFAULT_DATA_ROOT = str(f'{HOME_DIR}Inspyre-Softworks/{PROG}/')

print(DEFAULT_DATA_ROOT)

LOG_LEVELS = ['debug', 'info', 'warning', 'error']


