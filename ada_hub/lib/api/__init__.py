from ada_hub.lib.constants import PROG

from logging import getLogger

class Weather(object):

    def __init__(self):
        c_log_name = str(f'{PROG}.Weather')
        c_log = getLogger(c_log_name)
        c_log.debug(f'Logger initialized for {c_log_name}')

        # Alias the debug call that's so often used to a shorter variable to type
        self.log = c_log.debug

        c_log('Initializing an instance of Weather...')


