class ApplicationError(Exception):
    def __init__(self, err_type=None, *args, **kwargs):

        if 'err_type' in args[0]:
            err_type = args[0]['err_type']

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
