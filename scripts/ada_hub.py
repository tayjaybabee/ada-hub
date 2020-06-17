#!/usr/bin/env python3

import argparse
import os
import inspy_logger
import logging

from pathlib import Path
from platform import system as os_family

NAME = 'AdaHub'

get_logger = logging.getLogger

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


def write_pid():

    log = get_logger(f'{NAME}.write_pid')

    if 'linux' in os_family().lower():
        log.debug('Detected linux system')
        h_path = Path.home()
        log.debug(f'Detected {h_path} as home directory')
        data_dir = str(h_path) + '/Inspyre-Softworks/AdaHub/'
        log.debug(f'Therefore {data_dir} is where application data should be unless otherwise specified')



    pid = os.getpid()





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
                                help='Instruct the logger to suppress all logger messages below WARNING level from being '
                                     'output to the console',
                                required=False)

    verbosity_args.add_argument('-s', '--silent', action='store_true',
                                help='Instruct the logger to suppress all logger messages from being output to the '
                                     'console unless they are describing a fatal exception.',
                                required=False)

    subparsers = parser.add_subparsers(title='Sub-Commands',
                                       description='Valid sub-commands for ada-hub')

    cli_subparser = subparsers.add_parser('cli', help='Run a quick query using the command line (no GUI)')

    cli_subparser.add_argument('-l', '--location', type=int, action='store')

    parser.add_argument('-c', '--config-file', action='store', type=argparse.FileType('r'),
                        help='Provide the filesystem-location for a settings.ini file')

    return parser.parse_args()

def main():
    """

    This is the script's main entry point. If you have to call a function of this script directly for some reason
    you'd call on this function.

    Returns:

    """
    args = parse_args()

    start_logger(args)
    write_pid()

if __name__ == '__main__':
    main()
