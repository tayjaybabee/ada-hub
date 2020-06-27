"""

A module containing some constants for AdaHub's runtime.

"""

from platform import system
from os import getpid
from pathlib import Path

# Introduce constants containing the URL to the ada-hub repository on Github, and then concatenate that with
# '/issues/new' to form the URL to create a new issue. Both of these can be used when informing a user
REPO_URL = 'https://github.com/tayjaybabee/ada-hub'
ISSUE_URL = f'{REPO_URL}/issues/new'

PROG = 'AdaHub'
PID = getpid()

HOME_DIR = f'{ Path.home() }/'

DEFAULT_DATA_ROOT = str(f'{HOME_DIR}Inspyre-Softworks/{PROG}/')
DEFAULT_CONF_ROOT = str(f'{DEFAULT_DATA_ROOT}conf/')
DEFAULT_RUN_ROOT = str(f'{DEFAULT_DATA_ROOT}run/')

default_conf_file_name = 'settings'
default_conf_file_ext = 'ini'
DEFAULT_CONF_FILE_PATH = str(f'{DEFAULT_CONF_ROOT}{default_conf_file_name}.{default_conf_file_ext}')

LOG_LEVELS = ['debug', 'info', 'warning', 'error']


