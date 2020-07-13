#!/usr/bin/env python3

import argparse
import os
import inspy_logger
import logging

from pathlib import Path
from platform import system as os_family

from ada_hub.lib.constants import HOME_DIR, DEFAULT_DATA_ROOT
from ada_hub.lib.helpers.pid import write_pid
from ada_hub.lib.config import AdaHubConfig
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
    parser = argparse.ArgumentParser('ada-hub')

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

    # Create the 'credits' sub-command. This will be the command a user uses in order to see all the third-party
    # APIs, media, etc that are used in the operation of of the AdaHub application.
    credits_subparser = subparsers.add_parser('credits', help='Print out the credits for all external '
                                                              'services/software used to make Ada Hub')

    # Add an argument to the 'credits' sub-command that will clear the active terminal screen before outputting the
    # credits in order to improve readability, etc
    credits_subparser.add_argument('-c', '--clear-screen',
                                   action='store_true',
                                   default=False,
                                   help='Clear the terminal before printing the credits')

    cli_subparser = subparsers.add_parser('cli', help='Run a quick query using the command line (no GUI)')

    cli_subparser.add_argument('-l', '--location', type=int, action='store')

    # Create the 'GUI' sub-command. This will be the command a user uses to start the program in graphical mode.
    gui_subparser = subparsers.add_parser('gui', help='Start the program with the full GUI')

    # Add an argument to the 'GUI' sub-command that will instruct the program to start the SenseHat emulator instead
    # of attempting to find an attached HAT. This in-turn starts a graphical program so this will only be available
    # if the user is running AdaHub in graphical mode.
    gui_subparser.add_argument('-e', '--emulator', help='Start the Ada Hub application with the Sense-Emu backend.',
                               default=False)

    gui_subcommands = gui_subparser.add_subparsers(title='GUI Specific Commands', dest='gui_command',
                                                   help='Sub-commands specific to information or manipulation of the '
                                                        'Graphical User Interface?')

    gui_subcommands.add_parser('list-themes', help='Print out a list of strings that contain a list of acceptable '
                                                   'theme names, and then quits. (Useful for if you want to specify a '
                                                   'theme in your program-opening commands')


    # Add a global argument to allow input of a custom data-directory location.
    parser.add_argument('-D', '--data-dir', action='store', type=argparse.FileType('w'),
                        help="Provide the filesystem-location of your application's data directory, "
                             "or the destination you want the program to create a data-directory in.",
                        required=False)

    # Add a global argument to allow input of a custom config-directory location.
    parser.add_argument('-C', '--config-dir', action='store', type=argparse.FileType('w'),
                        help="Provide the filesystem-location of your application's configuration directory, "
                             "or the destination you want the program to create a configuration directory in.",
                        required=False)

    return parser.parse_args()


def main():
    from time import sleep
    """

    This is the script's main entry point. If you have to call a function of this script directly for some reason
    you'd call on this function.

    Returns:

    """
    args = parse_args()

    mode = args.command

    log = start_logger(args)

    sleep(0.02)

    log.debug(f'Starting Ada Hub in mode: {mode.upper()}')
    log.debug(f'Started Ada Hub with the following command-line args: {args}')

    from ada_hub.errors import ConnectivityError

    config = AdaHubConfig(args.config_dir)
    config = config.config

    if mode == 'credits':
        from ada_hub.lib.helpers.credits import third_party
        log.debug('Printing credits as directed...')
        third_party(config)
        log.debug('Exiting program')
        clean_exit(0, False)

    if args.data_dir:
        with open('conf_dir.txt', 'w') as f:
            f.write(args.data_dir)

    if args.data_dir is None:
        data_dir = DEFAULT_DATA_ROOT
    else:
        data_dir = args.data_dir

    connected = test_connection()

    if not connected:
        try:
            raise ConnectivityError('There seems to be no internet connection', err_type='No Connection')
        except ConnectivityError as e:
            log.error(e.message)

    pid_dir = str(f'{data_dir}run/')
    log.debug(f'Determined PID directory to be: {pid_dir}')
    write_pid(pid_dir)

    from ada_hub.lib.gui import GUIApp, GUIConfig

    gui_config = GUIConfig(config)

    GUIApp(gui_config.conf, args)


if __name__ == '__main__':
    main()