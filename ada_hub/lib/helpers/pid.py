from pathlib import Path
from logging import getLogger

from ada_hub.lib.constants import PROG as NAME, DEFAULT_DATA_ROOT

get_logger = getLogger
main_log = get_logger(f'{NAME}.{__file__.__name__}')
main_log.debug('pid.py has been imported.')



def remove_pid(data_root=None):
    pass


def write_pid(pid_filepath=None):
    pass

