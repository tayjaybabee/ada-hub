from ada_hub.lib.constants import PROG as NAME, DEFAULT_DATA_ROOT
from logging import getLogger as get_logger
import logging


def delete_pid():
    from ada_hub.lib.helpers.pid import remove_pid

    remove_pid()


def clean_exit(status):
    log = get_logger(f'{NAME}.clean_exit')
    if status == 1:
        log.setLevel(logging.DEBUG)
        log.debug('Received clean-exit call after a failure. Please check the logs above.')

    if status == 0:
        log.debug('Exit is expected. No errors.')

    log.info("User's desire to exit has been noted.")
    delete_pid()
    exit()
