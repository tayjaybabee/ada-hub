#!/usr/bin/env python3

import argparse
import os
import inspy_logger
import logging

from pathlib import Path
from platform import system as os_family

from ada_hub.lib.constants import HOME_DIR, DEFAULT_DATA_ROOT
from ada_hub.lib.helpers.pid import write_pid
from ada_hub.lib.helpers.config import load_config, create_config_file
from ada_hub.errors import ConnectivityError
from ada_hub import clean_exit

NAME = 'AdaHub'

get_logger = logging.getLogger


def test_connection():
    from ada_hub.lib.helpers.network import conn_test

    return conn_test()


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

    write_ok_args = parser.add_mutually_exclusive_group(required=False)

    write_ok_args.add_argument('-W', '--write-all',
                               required=False,
                               action='store_true',
                               default=False,
                               help='Write all files, regardless of location until permission fail')

    write_ok_args.add_argument('-w', '--write-data-dir',
                               required=False,
                               action='store_true',
                               default=True,
                               help=f'Write all files and directories in the configured data directory structure. By '
                                    f'default this directory is {DEFAULT_DATA_ROOT}')

    subparsers = parser.add_subparsers(title='Sub-Commands',
                                       dest='command',
                                       description='Valid sub-commands for ada-hub')

    credits_subparser = subparsers.add_parser('credits', help='Print out the credits for all external '
                                                              'services/software used to make Ada Hub')

    credits_subparser.add_argument('-c', '--clear-screen',
                                   action='store_true',
                                   default=False,
                                   help='Clear the terminal before printing the credits')

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
    log.debug(f'Started Ada Hub with the following command-line args: {args}')

    if mode == 'credits':
        from ada_hub.lib.credits import show
        log.debug('Printing credits as directed...')
        show()
        log.debug('Exiting program')
        clean_exit(0)

    if args.data_dir:
        with open('conf_dir.txt', 'w') as f:
            f.write(args.data_dir)

    if args.data_dir is None:
        data_dir = DEFAULT_DATA_ROOT
    else:
        data_dir = args.data_dir

    conf_dir_path = data_dir + 'conf/'
    conf_file_name = 'settings.ini'
    conf_file_path = conf_dir_path + conf_file_name

    if os.path.exists(data_dir):
        log.debug(f'{data_dir} exists, looking for existing config file.')
        if os.path.isfile(conf_file_path):
            log.debug(f'Found {conf_file_path}')
            config = load_config(conf_file_path)
    else:
        log.debug(f'Making configuration directory: {conf_dir_path}')
        os.makedirs(conf_dir_path)
        log.debug(f'Created!')

    if os.path.isfile(conf_file_path):
        log.debug(f'Found {conf_file_path}')
        config = load_config(conf_file_path)
    else:
        log.debug(f'Could not find {conf_file_path}')
        log.debug('Calling config file creator')
        create_config_file(str(f'{data_dir}conf/settings.ini'))

    connected = test_connection()

    if not connected:
        try:
            raise ConnectivityError('There seems to be no internet connection', err_type='No Connection')
        except ConnectivityError as e:
            log.error(e.message)

    pid_dir = str(f'{data_dir}run/')
    log.debug(f'Determined PID directory to be: {pid_dir}')
    write_pid(pid_dir)

    from ada_hub.lib.gui.models.windows.main_window import start as start_window

    start_window()


if __name__ == '__main__':
    main()
