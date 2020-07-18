from ada_hub.lib.constants import PROG

from logging import getLogger

class Allto(object):
    # Docstrings here

    def check_config(self):


    def __init__(self, cli_args):
        # ToDO:
        #   - Add docstring
        self.log_name = str(f'{PROG}.ALLTO')
        log = getLogger(self.log_name)
        debug = log.debug
        debug(f'Initializing {__class__.__name__}...')
