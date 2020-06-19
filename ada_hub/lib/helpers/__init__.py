"""

A package containing a few tools to help the main code.

"""

from platform import system as os_family
from pathlib import Path
import os
from logging import getLogger

from ada_hub.lib.constants import PROG as NAME, HOME_DIR, DEFAULT_DATA_ROOT

get_logger = getLogger

# def write_pid(data_dir):
#     log = get_logger(f'{NAME}.write_pid')
#
#     if data_dir is None:
#         data_dir = Path(HOME_DIR)
#
#
#     if 'linux' in os_family().lower():
#         log.debug('Detected linux system')
#         h_path = Path.home()
#         log.debug(f'Detected {h_path} as home directory')
#         data_dir = str(h_path) + '/Inspyre-Softworks/AdaHub/'
#         log.debug(f'Therefore {data_dir} is where application data should be unless otherwise specified')
#         pid = os.getpid()
#         log.info(f'My PID is {pid}')
#
#         data_dir = Path(data_dir)
#         if data_dir.exists():
#             log.debug(f'Found {data_dir}')
#         else:
#             log.info(f'Could not find {data_dir}, creating...')
#             os.makedirs(data_dir)
#             if not data_dir.exists():
#                 raise PermissionError(f'{data_dir} could not be created!')
#             else:
#                 log.debug(f'Successfully created {data_dir}')

