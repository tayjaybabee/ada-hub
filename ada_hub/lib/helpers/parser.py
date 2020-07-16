import argparse


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
                               type=bool,
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

    return parser
