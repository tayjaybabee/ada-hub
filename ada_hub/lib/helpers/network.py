"""

A module as part of the AdaHub.lib.helpers package that contains functions pertaining to network status,
connectivity, etc

"""
from ada_hub.lib.constants import PROG

import socket
from logging import getLogger

m_log_name = f'{PROG}.Helpers.Network'
m_log = getLogger(m_log_name)
m_log.debug(f'Imported and started logger for: {m_log_name}')


def backup_test():
    """

    A method to really figure out if there's no connection to the outside network. Basically pings https://inspyre.tech

    Returns:
        bool: Were we able to ping https://inspyre.tech? True for yes, False for no

    """
    import urllib.request  # We import this here because there's no need to bring this library into memory without
                           # calling this particular function

    # Try using the urllib.request library to connect to https://inspyre.tech. If we're unable to reach it,
    # urllib.request's 'urllopen' function will return an exception. Therefore, upon exception we return False
    try:
        urllib.request.urlopen('https://inspyre.tech')
        return True
    except:  # Sloppy, I know.
        return False

    #     |
    # TJB v
    # ToDo:
    #     - Find out what exception is raised if urlopen can't connect to a target
    #         - Handle that particular exception in the 'try' statement above.
    #             - If the exception is anything other than the exception that means urlopen failed to reach the
    #             requested host then re-raise the exception and exit_cleanly with a non-zero status code.


def conn_test():
    """

    A function to check if there's an internet connection.

    Returns:
        bool: Is there an internet connection? True if yes, False if no.

    """

    # Set up the logger, and announce self if the log output-level is at the proper level
    log_name = f'{m_log_name}.conn_test'
    log = getLogger(log_name)
    log.debug('Received request to check internet connectivity')

    # Grab the ip_address
    ip_address = socket.gethostbyname(socket.gethostname())
    log.debug(f'Determined IP address is {ip_address}')

    # Based on the IP address, determine if we should run a backup connectivity check, actually reaching outside the
    # network
    if ip_address == "127.0.0.1":
        log.warning(f'IP Address {ip_address} indicates a lack of internet connectivity')
        log.info('Running a backup network connectivity check.')
        if backup_test():
            log.info('Backup test was a success...')
            return True
        else:
            log.warning('Backup check failed as well. Failing out...')
            return False
    else:
        log.debug('We have an internet connection')
        return True
