#!/usr/bin/env python3

import argparse
import os
import inspy_logger
import logging

from pathlib import Path
from platform import system as os_family

from ada_hub.lib.constants import HOME_DIR
from ada_hub.lib.helpers.pid import write_pid


NAME = 'AdaHub'

get_logger = logging.getLogger


def clean_exit(status):
    # This
    log = get_logger(f'{NAME}.clean_exit')
    if status == 1:
        log.setLevel(logging.DEBUG)
        log.debug('Received clean-exit call after a failure. Please check the logs above.')


def start_logger(args):
    global get_logger

    is_verbose = False

    if args.verbose:
        is_verbose = True

    if args.debug:
        is_verbose = True

    device = inspy_logger.start(name='AdaHub', debug=is_verbose)
    device.debug('Logger started for AdaHub (raw device test)')
    log = logging.getLogger(f'{NAME}.start_logger')
    log.info('Started logger')

    return device


def remove_pid():
    pass


def parse_args():
    """

    Parse/define command-line arguments

    Returns:

    """
    parser = argparse.ArgumentParser('AdaHub')

    verbosity_args = parser.add_mutually_exclusive_group(required=False)

    verbosity_args.add_argument('-v', '--verbose', action='store_true',
                                help='Instruct the logger to output all messages below debug level to the console',
                                required=False)

    verbosity_args.add_argument('-d', '--debug', action='store_true',
                                help='Instruct the logger to output all messages it has to the console',
                                required=False)

    verbosity_args.add_argument('-q', '--quiet', action='store_true',
                                help='Instruct the logger to suppress all logger messages below WARNING level from '
                                     'being '
                                     'output to the console',
                                required=False)

    verbosity_args.add_argument('-s', '--silent', action='store_true',
                                help='Instruct the logger to suppress all logger messages from being output to the '
                                     'console unless they are describing a fatal exception.',
                                required=False)

    subparsers = parser.add_subparsers(title='Sub-Commands',
                                       dest='command',
                                       description='Valid sub-commands for ada-hub')

    cli_subparser = subparsers.add_parser('cli', help='Run a quick query using the command line (no GUI)')

    cli_subparser.add_argument('-l', '--location', type=int, action='store')

    gui_subparser = subparsers.add_parser('gui', help='Start the program with the full GUI')

    gui_subparser.add_argument('-e', '--emulator', help='Start the Ada Hub application with the Sense-Emu backend.',
                               default=False)

    parser.add_argument('-D', '--data-dir', action='store', type=argparse.FileType('w'),
                        help="Provide the filesystem-location of your application's data directory, "
                             "or the destination you want the program to create a data-directory in.")

    return parser.parse_args()


def main():
    """

    This is the script's main entry point. If you have to call a function of this script directly for some reason
    you'd call on this function.

    Returns:

    """
    args = parse_args()

    mode = args.command

    log = start_logger(args)

    log.debug(f'Starting Ada Hub in mode: {mode.upper()}')

    try:
        write_pid(args.data_dir)
    except PermissionError as e:
        log.error(e)
        clean_exit(status=1)

    from ada_hub.lib.gui.models.windows.main_window import start as start_window

    start_window()



if __name__ == '__main__':
    main()
