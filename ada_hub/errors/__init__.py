from logging import getLogger as get_logger

import inspect
import sys

NAME = 'AdaHub'

m_log = get_logger(NAME)
m_log.debug('Imported!')


class ApplicationError(Exception):
    def __init__(self, *args, **kwargs):


        if 'err_type' in args[1]:
            err_type = args[1]['err_type']

        if err_type is None:
            self.err_type = 'Unknown'
        else:
            self.err_type = err_type

        err_type = err_type.replace(' ', '%20')
        statement = f'An error of type {err_type} has occurred'
        print(statement)


class ConnectivityError(ApplicationError):
    def __init__(self, message=None, *args, **kwargs):

        super().__init__(args, kwargs)

        if message is None:
            self.message = "Unable to assess IP Address, this likely indicates that there's no internet connectivity"
        else:
            self.message = message


class FileStateDeSyncError(ApplicationError):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


m_log.debug(f'Imported {__file__}')
members = inspect.getmembers(sys.modules[__name__], inspect.isclass)
m_log.debug(f'This introduces the following classes: {members}')
print(members)
