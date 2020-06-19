"""

A module containing some constants for AdaHub's runtime.

"""

from platform import system
from os import getpid
from pathlib import Path

PROG = 'AdaHub'
PID = getpid()

HOME_DIR = Path.home()

DEFAULT_DATA_ROOT = str(f'{HOME_DIR}Inspyre-Softworks/{PROG}/')

LOG_LEVELS = ['debug', 'info', 'warning', 'error']


