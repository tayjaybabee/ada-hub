"""

A module for the AdaHub.lib.helpers package that contains functions to print out the credits

"""

class CreditsError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class NoCreditsFileError(CreditsError):
    def __init__(self, *args, **kwargs):
        from time import sleep
        super().__init__(args, kwargs)
        if 'message' in kwargs:
            self.message = kwargs['message']
        else:
            self.message = 'There is no credits file to read from. Please see support.'


def third_party(config):
    from os import path
    from time import sleep
    from pathlib import Path

    from ada_hub.lib.constants import PROG

    data_root = config.config['RUNTIME']['data_root_path']

    credits_path = Path('../CREDITS').absolute()
    print(credits_path)

    if path.isfile(credits_path):
        with open(credits_path, 'r') as file:
            for line in file.readlines():
                sleep(.5)
                print(line)

    else:
        try:
            raise NoCreditsFileError(message='Credits file missing!')
        except NoCreditsFileError as e:
            print(e.message)
            exit(1)



