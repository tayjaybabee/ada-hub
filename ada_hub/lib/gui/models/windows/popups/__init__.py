from logging import getLogger
import PySimpleGUIQt as Qt

from ada_hub.lib.constants import PROG

# Start a logger and (for debugging purposes) announce that we've been imported.
m_log = getLogger(PROG)
m_log.debug(f'I\'ve been imported! ({__file__})')

title_prefix = 'AdaHub | Error'

def not_yet_implemented(feature=None):
    """

        Produce a popup window that notifies the user that they have attempted to activate a feature that is not yet
        implemented. This error would usually occur after attempting to activate a feature that has an
        interactive placeholder for a part of the program that has not yet had it's code written, etc.

        Returns:
            None

    """

    if feature is not None:
        feature = feature.strip()
    else:
        feature = 'This feature'

    statement = str(f'{feature} is not yet implemented.')

    Qt.PopupError(statement, title=f'{title_prefix} | Not Yet Implemented', keep_on_top=True)


def no_internet_connection():
    """

    Produce a popup window that notifies the user of AdaHub's lack of ability to reliably establish a connection
    outside of the local network.

    Returns:
        None

    """

    log = getLogger(f'{PROG}.{__name__}')
    log.debug('Received request to produce popup to notify user that they attempted to activate a feature that has '
              'not yet been implemented.')

    statement = 'AdaHub was unable to find an internet connection.\n' \
                '\nPlease check your connection.'

    Qt.PopupError(statement, title=f'{title_prefix}', keep_on_top=True)


def continue_anyway(issue):

    # Set-up the logger
    log = getLogger(f'{PROG}.{__name__}')
    log.debug('Received request to produce a "continue?" popup window.')

    # Provide a layout for our window
    logo_frame = [[Qt.Image('/home/taylor/Pictures/logo.png', key='img_elm')]]

    button_frame = [
            [Qt.Button('Yes')]
            ]

    main_layout = [
            [Qt.Frame('', layout=logo_frame, element_justification='center', size=(40, 40))],
            []
            ]

    window = Qt.Window('Continue Anyway?', layout=main_layout)


    while True:
        event, vals = window.read(timeout=100)



        if event is None or vals == 'exit':
            log.debug('User leaving window by click')



continue_anyway(dir())



