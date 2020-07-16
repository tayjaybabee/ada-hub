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
""" The name of the application """

PID = getpid()
""" The PID of the application """

HOME_DIR = f'{ Path.home() }/'
""" The user's home directory """

DEFAULT_DATA_ROOT = str(f'{HOME_DIR}Inspyre-Softworks/{PROG}/')
""" The default root directory for AdaHub's data"""

DEFAULT_CONF_ROOT = str(f'{DEFAULT_DATA_ROOT}conf/')
""" The default configuration directory for AdaHub """

DEFAULT_RUN_ROOT = str(f'{DEFAULT_DATA_ROOT}run/')
""" The default runtime working directory for AdaHub """

default_conf_file_name = 'settings'
default_conf_file_ext = 'ini'
DEFAULT_CONF_FILE_PATH = str(f'{DEFAULT_CONF_ROOT}{default_conf_file_name}.{default_conf_file_ext}')
""" The default filepath for AdaHubs configuration file. """

LOG_LEVELS = ['debug', 'info', 'warning', 'error']
""" The levels available to the logger. """
