from pathlib import Path
from logging import getLogger
from ada_hub.lib.constants import PROG as NAME, DEFAULT_DATA_ROOT, PID
from ada_hub.errors import FileStateDeSyncError

from ada_hub import clean_exit

import os

get_logger = getLogger
main_log = get_logger(f'{NAME}')
main_log.debug('Imported')
main_log.debug(f'My PID is: {PID}')

DEFAULT_RUN_DIR = str(f"{ DEFAULT_DATA_ROOT }run/")

run_dir = None


def write_pid(inc_run_dir=None):
    """

    A function that writes our PID to a file (by default $USER_DIR/Inspyre-Softworks/AdaHub/run/PID) for easy access
    during runtime.

    For example; if the program is un-responsive but you still have control over other applications in your system
    you can run:

    Args:
        inc_run_dir ():

    Returns:
        None
    """
    global run_dir

    log = get_logger(f'{NAME}.WritePID')
    log.debug(f'Started logger for {NAME}.WritePID')

    # If an argument was not provided for an incoming run directory (inc_run_dir) then the program defaults to using
    # the string stored in the c
    if inc_run_dir is None:
        log.debug(f'No run directory provided in parameters. Falling back to default: {DEFAULT_RUN_DIR}')
        run_dir = DEFAULT_RUN_DIR
    else:
        log.debug(f'Received run directory as a parameter with the value of {inc_run_dir}')
        run_dir = str(inc_run_dir)

    # Determine the filepath of the PID file
    pid_filepath = f'{run_dir}PID'
    log.debug(f'Writing PID to {pid_filepath}')

    # See if there is already a PID file present, if so; report it through a warning log and proceed. If a PID file
    # is not found then the program will create one
    if os.path.exists(run_dir):
        log.debug(f'Was able to find runtime directory: {run_dir}')
        log.debug(f'Looking for a PID file already present in target location...')
        if os.path.isfile(pid_filepath):
            log.debug(f'Found PID file at: {pid_filepath}')
            log.warning(f'Previous session did not close gracefully')
        else:
            log.debug(f'No PID file found in: {pid_filepath}')
            log.debug(f'Will now create PID file in: {pid_filepath}')

        # Write the PID to a file
        with open(pid_filepath, 'w') as file:
            file.write(str(PID))

        # Announce the program PID
        log.info(f'My PID is: {PID}')

    else:
        log.debug(f'{run_dir} does not exist. Creating.')
        os.makedirs(run_dir)
        log.debug('Starting function over now that run directory exists.')
        write_pid(run_dir)


def remove_pid():
    """

    A function that removes the PID file from the file-system.

    NOTE: It is best practice to only use this function when you know what you're doing.

    Returns:
        None

    """
    global run_dir
    name = str(f'{NAME}.Remove')
    log = get_logger(name)

    log.debug('Received request to remove PID file for shutdown')

    pid_filepath = f'{run_dir}PID'
    log.debug(f'PID file should be located at: {pid_filepath}')

    # Make sure the directory is still there to begin with. We'd rather error-out knowing at exactly which step and
    # why than just have a random permissions or file not found error when we try to work in this directory
    if os.path.exists(run_dir):
        log.debug(f'Was able to find {run_dir}')
    else:
        raise FileStateDeSyncError(err_type='FileDeSync')

    # Remove the present PID file, if there is one
    if os.path.isfile(pid_filepath):
        log.debug(f'Found {pid_filepath}')
        log.debug(f'Removing {pid_filepath}')
        os.remove(pid_filepath)
        log.debug('Done!')

        # Check to see if the file was really deleted, to avoid any anomalies. If it's still present, fail-out.
        if os.path.isfile(pid_filepath):
            log.error('File was not deleted!')
            clean_exit(1)
