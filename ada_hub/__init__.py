from ada_hub.lib.constants import PROG as NAME, DEFAULT_DATA_ROOT
from logging import getLogger as get_logger
import logging

m_name = f'{NAME}.Package'
m_log = get_logger(m_name)
m_log.debug(f'Imported {m_name}!')


def clean_exit(status, should_rem_pid=True):
    """

    A function that - when called - will cleanly exit the AdaHub application. On a clean exit the application will
    remove the saved PID file, and report it's status.

    Args:
        status (int): Either 1 or 0. 0 means everything went as expected. 1 means an error or exception occurred.

        should_rem_pid (bool): Should the program attempt to remove the file PID located in the program's 'run'
        directory? (Defaults to True)

    Returns:
        None

    """
    from .lib.helpers.pid import remove_pid

    log_name = f'{m_name}.clean_exit'
    log = get_logger(log_name)
    log.debug(f'Started logger for {log_name}')

    log.info("User's desire to exit has been noted.")

    log.debug(f'Exit status: {status}')
    log.debug(f'Intent to delete PID file? {should_rem_pid}')

    if status == 1:
        log.setLevel(logging.DEBUG)
        log.debug('Received clean-exit call after a failure. Please check the logs above.')

    if status == 0:
        log.debug('Exit is expected. No errors.')

    if should_rem_pid:
        log.debug('Removing PID file!')
        remove_pid()
        log.debug('PID file removed, exiting...')
    else:
        log.debug('Was instructed not to remove PID file.')
        log.debug('Exiting...')


    exit()
